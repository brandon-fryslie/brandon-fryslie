# LED Art Stack: Building a Hardware Art Pipeline

## Overview

Between 2018 and 2021, I built a multi-layer stack for controlling LED art installations, from ESP8266 microcontrollers to React interfaces for kinetic sculptures. This wasn't a single project—it was an evolving pipeline where each layer solved problems discovered in the previous one.

## The Pipeline

### Layer 1: Direct Control (2018-2021)

**[esp-bloom](https://github.com/brandon-fryslie/esp-bloom)** — Bias lighting using macOS screen capture to drive SK6812 RGBW LEDs via ESP8266 at 115200 baud. RGBW over RGB provided better luminosity precision for ambient lighting. Python-based color processing pipeline with serial communication.

### Layer 2: Network Sync (2021)

**[pb-sync](https://github.com/brandon-fryslie/pb-sync)** (2 stars) — Version control for LED patterns. TypeScript tool backing up `.epe` files and metadata from PixelBlaze WiFi LED controllers. Planned features include bi-directional sync, directory watching, and auto-upload.

**[Firestorm](https://github.com/brandon-fryslie/Firestorm)** — Centralized control for multiple PixelBlaze devices. Implements NTP-like time synchronization via UDP beacons leveraging PixelBlaze's discovery protocol. Client-driven sequence choreography with automatic recovery: disconnected devices receive cached commands within 5 minutes.

### Layer 3: Physical Installation (2018)

**[tesseract-react](https://github.com/brandon-fryslie/tesseract-react)** (2 stars, 3 forks) — React frontend controlling "Draco," a kinetic LED sculpture. Real physical art installation requiring Docker deployment for iPad and local network access. Integration with Processing backend via forked [tesseract_java](https://github.com/brandon-fryslie/tesseract_java) and [PixelPusher-java](https://github.com/brandon-fryslie/PixelPusher-java).

### Supporting Infrastructure

- **[LedPixelController fork](https://github.com/brandon-fryslie/LedPixelController)** — ESP8266 E1.31 protocol to WS2812 LED driver
- **[Firestorm fork](https://github.com/brandon-fryslie/Firestorm)** — PixelBlaze control console
- **[massdrop_orig_qmk_firmware](https://github.com/brandon-fryslie/massdrop_orig_qmk_firmware)** (2021) — Keyboard firmware, demonstrating hardware breadth beyond LEDs

## Technical Challenges

1. **Serial Bandwidth**: 115200 baud for real-time screen capture feedback loop
2. **Network Synchronization**: UDP beacon timing for distributed LED controller coordination
3. **Pattern Management**: Version control for binary `.epe` pattern files without standard diffing
4. **Physical Installation**: Network-accessible UI for real-world art gallery deployment

## Outcomes

- Working kinetic sculpture installation with web-based control
- Reusable sync infrastructure across multiple hardware projects
- PixelBlaze ecosystem contributions (pb-sync used by others in the community)
- Foundation for future installations requiring synchronized multi-controller setups

## Links

- [esp-bloom](https://github.com/brandon-fryslie/esp-bloom) — ESP8266 bias lighting
- [pb-sync](https://github.com/brandon-fryslie/pb-sync) — PixelBlaze version control
- [tesseract-react](https://github.com/brandon-fryslie/tesseract-react) — Kinetic sculpture frontend
- [Firestorm](https://github.com/brandon-fryslie/Firestorm) — Multi-controller synchronization
