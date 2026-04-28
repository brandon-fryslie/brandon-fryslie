// brandon-fryslie.github.io/brandon-fryslie/main.js
// The unconstrained Pages-side counterpart to the profile README. Same daily
// content engine drives both surfaces; this one elaborates beyond what the
// GitHub-sandboxed profile can express (real JS, fetch, WebGPU canvas).

const $ = (sel) => document.querySelector(sel);

async function detectWebGPU() {
  if (!navigator.gpu) return { ok: false, reason: 'navigator.gpu unavailable' };
  try {
    const adapter = await navigator.gpu.requestAdapter();
    if (!adapter) return { ok: false, reason: 'no adapter' };
    const device = await adapter.requestDevice();
    if (!device) return { ok: false, reason: 'no device' };
    return { ok: true, adapter, device };
  } catch (e) {
    return { ok: false, reason: e?.message ?? String(e) };
  }
}

function setRenderModeBadge(mode) {
  const el = $('#render-mode');
  if (!el) return;
  if (mode === 'webgpu') {
    el.textContent = 'render: WebGPU';
    el.classList.add('is-webgpu');
  } else {
    el.textContent = `render: SVG fallback`;
    el.classList.add('is-fallback');
  }
}

// Stub WebGPU hero — clears with a sky color matching the SVG palette so the
// transition from SVG-fallback to live render won't be jarring once the real
// procedural Flatirons shader lands. For now intentionally NOT swapped in;
// canvas stays display:none until the shader work is real.
async function initWebGPUHero(canvas, device) {
  const ctx = canvas.getContext('webgpu');
  const format = navigator.gpu.getPreferredCanvasFormat();
  ctx.configure({ device, format, alphaMode: 'opaque' });

  const resize = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.max(1, Math.floor(rect.width * dpr));
    canvas.height = Math.max(1, Math.floor(rect.height * dpr));
  };
  resize();
  window.addEventListener('resize', resize, { passive: true });

  function frame() {
    const encoder = device.createCommandEncoder();
    const pass = encoder.beginRenderPass({
      colorAttachments: [{
        view: ctx.getCurrentTexture().createView(),
        clearValue: { r: 0.184, g: 0.49, b: 0.75, a: 1.0 },
        loadOp: 'clear',
        storeOp: 'store',
      }],
    });
    pass.end();
    device.queue.submit([encoder.finish()]);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}

// Tiny markdown subset → HTML. Just enough for the daily content shapes
// (bullets with links, bold, paragraphs). When Pages outgrows this, swap in
// a real markdown lib — but every dependency you avoid is one less thing to
// re-cache and re-audit.
function md2html(md) {
  if (!md) return '';
  const lines = md.split('\n');
  const out = [];
  let inList = false;

  const inline = (s) => s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g,
      '<a href="$2" target="_blank" rel="noopener">$1</a>');

  for (let raw of lines) {
    const line = raw.trimEnd();
    if (!line.trim()) {
      if (inList) { out.push('</ul>'); inList = false; }
      continue;
    }
    const bullet = line.match(/^\s*-\s+(.*)$/);
    const heading = line.match(/^(#{1,4})\s+(.*)$/);
    if (heading) {
      if (inList) { out.push('</ul>'); inList = false; }
      const lvl = Math.min(heading[1].length + 1, 4);
      out.push(`<h${lvl}>${inline(heading[2])}</h${lvl}>`);
    } else if (bullet) {
      if (!inList) { out.push('<ul>'); inList = true; }
      out.push(`<li>${inline(bullet[1])}</li>`);
    } else {
      if (inList) { out.push('</ul>'); inList = false; }
      out.push(`<p>${inline(line)}</p>`);
    }
  }
  if (inList) out.push('</ul>');
  return out.join('\n');
}

function renderProjects(projectsMarkdown) {
  // The profile's SELECTED-PROJECTS region is a markdown table OR a list.
  // We try to parse a simple "**Name** — description" pattern first, falling
  // back to raw markdown if the shape doesn't match.
  if (!projectsMarkdown) return '';
  const lines = projectsMarkdown.split('\n').filter(l => l.trim().startsWith('-'));
  if (!lines.length) return md2html(projectsMarkdown);

  const cards = lines.map(line => {
    const m = line.match(/^\s*-\s+\*\*([^*]+)\*\*\s*[—\-:]?\s*(.*)$/);
    if (!m) return `<div class="project-card">${md2html(line)}</div>`;
    const [, name, desc] = m;
    const inline = (s) => s
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g,
        '<a href="$2" target="_blank" rel="noopener">$1</a>')
      .replace(/`([^`]+)`/g, '<code>$1</code>');
    return `<div class="project-card">
      <h3>${inline(name)}</h3>
      <p>${inline(desc)}</p>
    </div>`;
  });
  return cards.join('\n');
}

function applyDailyData(data) {
  const generated = data?.generated_at ? new Date(data.generated_at) : null;
  if (generated) {
    const stamp = generated.toISOString().slice(0, 10);
    $('#generated-at').textContent = `updated: ${stamp}`;
  }

  if (data?.tagline) $('#tagline').textContent = data.tagline;

  if (data?.intro?.html) {
    $('#intro-prose').innerHTML = data.intro.html;
  } else if (data?.intro?.markdown) {
    $('#intro-prose').innerHTML = md2html(data.intro.markdown);
  }

  if (data?.activity?.html) {
    $('#activity-content').innerHTML = data.activity.html;
  } else if (data?.activity?.markdown) {
    $('#activity-content').innerHTML = md2html(data.activity.markdown);
  }

  if (data?.projects?.markdown) {
    $('#projects-content').innerHTML = renderProjects(data.projects.markdown);
  } else if (data?.projects?.html) {
    $('#projects-content').innerHTML = data.projects.html;
  }

  if (data?.doodle?.svg_inline) {
    $('#doodle-content').innerHTML = data.doodle.svg_inline;
  } else if (data?.doodle?.svg_path) {
    $('#doodle-content').innerHTML =
      `<img src="${data.doodle.svg_path}" alt="Daily doodle">`;
  }
}

async function init() {
  const canvas = $('#hero-canvas');
  const fallback = $('#hero-fallback');

  const gpu = await detectWebGPU();
  if (gpu.ok) {
    // WebGPU is available — log it and prepare the device, but DON'T swap
    // the canvas in yet. The procedural Flatirons shader is the next big
    // piece of work; until it's ready, the SVG is the better visual.
    // Keeping this code path live (just hidden) means we can swap by flipping
    // one display rule once the shader exists.
    setRenderModeBadge('webgpu-ready');
    $('#render-mode').textContent = 'render: SVG (WebGPU ready)';
    $('#render-mode').classList.add('is-fallback');
    // Uncomment when shader is ready:
    // canvas.style.display = 'block';
    // fallback.style.display = 'none';
    // await initWebGPUHero(canvas, gpu.device);
  } else {
    setRenderModeBadge('fallback');
    console.info('WebGPU unavailable:', gpu.reason);
  }

  try {
    const res = await fetch('daily.json', { cache: 'no-cache' });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    applyDailyData(data);
  } catch (e) {
    console.warn('daily.json fetch failed:', e);
    $('#tagline').textContent = "Today's content didn't load — check the source repo for the latest.";
  }
}

init();
