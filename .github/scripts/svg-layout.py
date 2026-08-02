#!/usr/bin/env python3
"""
Deterministic layout-math helpers for the stats-card agent (.github/prompts/stats-card.md).

The agent composes SVG freely each day — that's the point, the card is required to be
a different concept every run. What is NOT supposed to vary day to day is whether the
underlying arithmetic is right: vertically centering text in a box, leaving clearance
above/below an element, checking a label fits its container, checking a color is
legible against its background. Every one of those is a pure function of a few
numbers, and every one of them has shown up as a real shipped bug (2026-08-01/02:
baseline set equal to a box's center instead of offset for it, a caption crammed
against a data-sized grid, a contrast ratio nobody computed). Re-deriving that
arithmetic from memory, fresh, in every daily run is exactly the situation
`[LAW:carrying-cost]` warns about: cheap to skip once, and it already produced three
distinct bugs from the same root cause in two days.

This tool is optional. Nothing requires the agent to use it, and it should not be used
for the creative/compositional decisions (concept, palette, motion, what to
visualize) — only for the mechanical coordinate math underneath whatever composition
the agent has already chosen. [LAW:composability]: every subcommand takes plain
scalars and returns one plain value; none of them know or assume anything about the
stats card's own layout, so they compose into any SVG the agent invents.

Text-width measurement note: widths come from a per-character advance-width table
sampled once (2026-08-02) from the local Helvetica/HelveticaNeue-Bold faces, as a
stand-in for the card's actual `-apple-system, ... sans-serif` stack — no exact match
exists across every viewer's actual browser/OS font substitution, so this is always an
approximation. It is frozen data, not a live Pillow/font dependency, so this script
stays stdlib-only and needs nothing installed in CI. Cross-checking summed
advance-widths (this table's method) against real whole-string measurement showed up
to ~7% underestimate from ignoring kerning, before any cross-viewer font variance is
even considered — `fits` bakes in a real safety margin for exactly this reason; don't
trust `text-width` output to the pixel.
"""

import argparse
import sys

# Sampled 2026-08-02 from /System/Library/Fonts/Helvetica.ttc (regular) and
# HelveticaNeue.ttc bold face, at 1000-units-per-em (the standard font-metrics
# convention) so any font-size scales by simple division. See module docstring for
# the accuracy caveat — this is a frozen approximation, not exact per-viewer metrics.
REGULAR_WIDTHS = {" ":280.0,"!":280.0,"\"":355.0,"#":555.0,"$":555.0,"%":890.0,"&":665.0,"'":190.0,"(":335.0,")":335.0,"*":390.0,"+":585.0,",":280.0,"-":335.0,".":280.0,"/":280.0,"0":555.0,"1":555.0,"2":555.0,"3":555.0,"4":555.0,"5":555.0,"6":555.0,"7":555.0,"8":555.0,"9":555.0,":":280.0,";":280.0,"<":585.0,"=":585.0,">":585.0,"?":555.0,"@":1015.0,"A":665.0,"B":665.0,"C":720.0,"D":720.0,"E":665.0,"F":610.0,"G":780.0,"H":720.0,"I":280.0,"J":500.0,"K":665.0,"L":555.0,"M":835.0,"N":720.0,"O":780.0,"P":665.0,"Q":780.0,"R":720.0,"S":665.0,"T":610.0,"U":720.0,"V":665.0,"W":945.0,"X":665.0,"Y":665.0,"Z":610.0,"[":280.0,"\\":280.0,"]":280.0,"^":470.0,"_":555.0,"`":335.0,"a":555.0,"b":555.0,"c":500.0,"d":555.0,"e":555.0,"f":280.0,"g":555.0,"h":555.0,"i":220.0,"j":220.0,"k":500.0,"l":220.0,"m":835.0,"n":555.0,"o":555.0,"p":555.0,"q":555.0,"r":335.0,"s":500.0,"t":280.0,"u":555.0,"v":500.0,"w":720.0,"x":500.0,"y":500.0,"z":500.0,"{":335.0,"|":260.0,"}":335.0,"~":585.0,"·":280.0}
BOLD_WIDTHS = {" ":280.0,"!":280.0,"\"":465.0,"#":555.0,"$":555.0,"%":1000.0,"&":685.0,"'":280.0,"(":295.0,")":295.0,"*":405.0,"+":600.0,",":280.0,"-":405.0,".":280.0,"/":370.0,"0":555.0,"1":555.0,"2":555.0,"3":555.0,"4":555.0,"5":555.0,"6":555.0,"7":555.0,"8":555.0,"9":555.0,":":280.0,";":280.0,"<":600.0,"=":600.0,">":600.0,"?":555.0,"@":800.0,"A":685.0,"B":705.0,"C":740.0,"D":740.0,"E":650.0,"F":595.0,"G":760.0,"H":740.0,"I":295.0,"J":555.0,"K":720.0,"L":595.0,"M":905.0,"N":740.0,"O":780.0,"P":665.0,"Q":780.0,"R":720.0,"S":650.0,"T":610.0,"U":740.0,"V":630.0,"W":945.0,"X":665.0,"Y":665.0,"Z":650.0,"[":335.0,"\\":370.0,"]":335.0,"^":600.0,"_":500.0,"`":260.0,"a":575.0,"b":610.0,"c":575.0,"d":610.0,"e":575.0,"f":335.0,"g":610.0,"h":595.0,"i":260.0,"j":280.0,"k":575.0,"l":260.0,"m":905.0,"n":595.0,"o":610.0,"p":610.0,"q":610.0,"r":390.0,"s":535.0,"t":350.0,"u":595.0,"v":520.0,"w":815.0,"x":535.0,"y":520.0,"z":520.0,"{":335.0,"|":225.0,"}":335.0,"~":600.0,"·":280.0}

# Cap-height and descender depth as a fraction of font-size, Helvetica-family. Used by
# center-y and clear — these ratios don't meaningfully shift between regular and bold
# (bold changes stroke width and advance, not vertical proportions), so unlike
# text-width/fits neither subcommand takes a --weight.
CAP_HEIGHT_RATIO = 0.72
DESCENDER_RATIO = 0.20


def text_width(text, font_size, weight):
    table = BOLD_WIDTHS if weight >= 700 else REGULAR_WIDTHS
    units = sum(table.get(ch, table[" "]) for ch in text)
    return units / 1000 * font_size


def contrast_ratio(hex1, hex2):
    def to_rgb(h):
        h = h.lstrip("#")
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    def luminance(rgb):
        def lin(c):
            c = c / 255
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        r, g, b = (lin(c) for c in rgb)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    l1, l2 = luminance(to_rgb(hex1)), luminance(to_rgb(hex2))
    l1, l2 = max(l1, l2), min(l1, l2)
    return (l1 + 0.05) / (l2 + 0.05)


def cmd_text_width(args):
    print(round(text_width(args.text, args.font_size, args.weight), 1))


def cmd_fits(args):
    w = text_width(args.text, args.font_size, args.weight)
    effective = args.width * (1 - args.slack_pct / 100)
    margin = effective - w
    fits = margin >= 0
    print(f"width={w:.1f} available={args.width:.1f} "
          f"effective_after_{args.slack_pct:g}pct_slack={effective:.1f} "
          f"fits={'yes' if fits else 'no'} margin={margin:.1f}")
    if not fits:
        print(f"OVERFLOW: '{args.text}' needs {w:.1f}px, only {effective:.1f}px "
              f"available after reserving {args.slack_pct:g}% slack for cross-viewer "
              f"font substitution — shorten the text, shrink the font, or move it "
              f"outside the container.", file=sys.stderr)
    return 0 if fits else 1


def cmd_center_y(args):
    box_center = args.box_top + args.box_height / 2
    offset = (CAP_HEIGHT_RATIO - DESCENDER_RATIO) / 2 * args.font_size
    baseline = box_center + offset
    print(round(baseline, 1))


def cmd_clear(args):
    if args.side == "below":
        # anchor is the BOTTOM edge of whatever sits above; the new text's cap-height
        # must clear `gap` px of space below that edge before its glyphs start.
        baseline = args.anchor + args.gap + CAP_HEIGHT_RATIO * args.font_size
    else:
        # anchor is the TOP edge of whatever sits below; the new text's descenders
        # must clear `gap` px of space above that edge.
        baseline = args.anchor - args.gap - DESCENDER_RATIO * args.font_size
    print(round(baseline, 1))


def cmd_contrast(args):
    ratio = contrast_ratio(args.hex1, args.hex2)
    print(round(ratio, 2))
    if args.min is not None and ratio < args.min:
        print(f"BELOW MINIMUM: {ratio:.2f}:1 < required {args.min:g}:1 for "
              f"'{args.hex1}' on '{args.hex2}' — pick a color with more contrast or "
              f"increase font-size/weight.", file=sys.stderr)
        return 1
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("text-width", help="estimated rendered width of a string, in px")
    sp.add_argument("text")
    sp.add_argument("--font-size", type=float, required=True)
    sp.add_argument("--weight", type=int, default=400, help="400 or 700 (default 400)")
    sp.set_defaults(func=cmd_text_width)

    sp = sub.add_parser("fits", help="does this text fit a given width, with safety slack?")
    sp.add_argument("text")
    sp.add_argument("--width", type=float, required=True, help="available width in px")
    sp.add_argument("--font-size", type=float, required=True)
    sp.add_argument("--weight", type=int, default=400, help="400 or 700 (default 400)")
    sp.add_argument("--slack-pct", type=float, default=18,
                     help="safety margin reserved for cross-viewer font substitution "
                          "and this table's own ~7%% kerning error (default 18)")
    sp.set_defaults(func=cmd_fits)

    sp = sub.add_parser("center-y", help="baseline y that vertically centers text in a box")
    sp.add_argument("--box-top", type=float, required=True)
    sp.add_argument("--box-height", type=float, required=True)
    sp.add_argument("--font-size", type=float, required=True)
    sp.set_defaults(func=cmd_center_y)

    sp = sub.add_parser("clear", help="baseline y that clears `gap` px from an anchor edge")
    sp.add_argument("--anchor", type=float, required=True,
                     help="the anchor edge y: the BOTTOM of the element above (side=below) "
                          "or the TOP of the element below (side=above)")
    sp.add_argument("--gap", type=float, required=True, help="desired visual clearance in px")
    sp.add_argument("--font-size", type=float, required=True)
    sp.add_argument("--side", choices=["below", "above"], required=True,
                     help="'below': this text sits below the anchor. "
                          "'above': this text sits above the anchor.")
    sp.set_defaults(func=cmd_clear)

    sp = sub.add_parser("contrast", help="WCAG contrast ratio between two hex colors")
    sp.add_argument("hex1")
    sp.add_argument("hex2")
    sp.add_argument("--min", type=float, default=None,
                     help="if given, exit 1 when the ratio is below this")
    sp.set_defaults(func=cmd_contrast)

    args = p.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
