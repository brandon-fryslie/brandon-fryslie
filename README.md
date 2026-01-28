<div align="center">

<!-- Animated Header SVG -->
<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1">
        <animate attributeName="stop-color" values="#00D9FF;#7B68EE;#FF1493;#00D9FF" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#7B68EE;stop-opacity:1">
        <animate attributeName="stop-color" values="#7B68EE;#FF1493;#00D9FF;#7B68EE" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#FF1493;stop-opacity:1">
        <animate attributeName="stop-color" values="#FF1493;#00D9FF;#7B68EE;#FF1493" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Animated circles background -->
  <circle cx="100" cy="100" r="30" fill="url(#grad1)" opacity="0.3">
    <animate attributeName="r" values="30;50;30" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.3;0.6;0.3" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="100" r="40" fill="url(#grad1)" opacity="0.3">
    <animate attributeName="r" values="40;60;40" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.3;0.6;0.3" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="400" cy="50" r="20" fill="url(#grad1)" opacity="0.4">
    <animate attributeName="r" values="20;35;20" dur="2.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.4;0.7;0.4" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Main text -->
  <text x="400" y="110" font-family="'Courier New', monospace" font-size="48" font-weight="bold" 
        fill="url(#grad1)" text-anchor="middle" filter="url(#glow)">
    BRANDON FRYSLIE
    <animate attributeName="opacity" values="1;0.7;1" dur="2s" repeatCount="indefinite"/>
  </text>
  
  <text x="400" y="145" font-family="'Courier New', monospace" font-size="20" 
        fill="#00D9FF" text-anchor="middle">
    Senior Software Engineer • AI/ML • Open Source
  </text>
  
  <!-- Animated underline -->
  <line x1="150" y1="160" x2="650" y2="160" stroke="url(#grad1)" stroke-width="3">
    <animate attributeName="stroke-dasharray" values="0,500;500,0" dur="2s" repeatCount="indefinite"/>
  </line>
</svg>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=00D9FF&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=80&lines=Building+the+future%2C+one+commit+at+a+time;70%2B+repositories+%7C+10%2B+years+experience;%22Stay+green%2C+keep+growing%22)](https://git.io/typing-svg)

</div>

---

## 🚀 About Me

```javascript
const brandon = {
    location: "🌎 Earth",
    languages: ["Python", "JavaScript", "TypeScript", "Shell", "PHP", "CoffeeScript"],
    expertise: {
        ai_ml: ["OpenAI APIs", "LLMs", "TTS/STT", "AI Integration"],
        fullstack: ["React", "Node.js", "Express", "REST APIs", "WebSockets"],
        devtools: ["CLI Tools", "Zsh", "Terminal Productivity", "Dev Experience"],
        devops: ["Docker", "CI/CD", "Automation", "Infrastructure"],
        creative: ["IoT", "ESP8266", "LED Programming", "Hardware Integration"]
    },
    currentFocus: "🤖 AI-powered developer tools & experiences",
    philosophy: "If you're green, you're growing. If you're ripe, you're rotten.",
    funFact: "I built a Zsh framework used by thousands of developers! 🎯"
};
```

<div align="center">

<!-- Animated Divider -->
<svg width="100%" height="40" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1">
        <animate attributeName="offset" values="0;1;0" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#7B68EE;stop-opacity:1">
        <animate attributeName="offset" values="0.5;1;0.5" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#FF1493;stop-opacity:1">
        <animate attributeName="offset" values="1;0;1" dur="3s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
  </defs>
  <rect width="100%" height="4" fill="url(#lineGrad)" y="18"/>
</svg>

</div>

---

## 🔥 Featured Projects

<div align="center">

<!-- Animated Project Showcase SVG -->
<svg width="100%" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="projectGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.8"/>
      <stop offset="100%" style="stop-color:#7B68EE;stop-opacity:0.8"/>
    </linearGradient>
  </defs>
  
  <!-- Animated hexagons -->
  <polygon points="60,20 90,35 90,65 60,80 30,65 30,35" fill="url(#projectGrad)" opacity="0.6">
    <animateTransform attributeName="transform" type="rotate" from="0 60 50" to="360 60 50" dur="10s" repeatCount="indefinite"/>
  </polygon>
  
  <polygon points="160,20 190,35 190,65 160,80 130,65 130,35" fill="url(#projectGrad)" opacity="0.5">
    <animateTransform attributeName="transform" type="rotate" from="360 160 50" to="0 160 50" dur="8s" repeatCount="indefinite"/>
  </polygon>
  
  <text x="50%" y="55" font-family="Arial, sans-serif" font-size="28" font-weight="bold" 
        fill="#00D9FF" text-anchor="middle">
    🚀 SHOWCASE 🚀
  </text>
  
  <text x="50%" y="85" font-family="Arial, sans-serif" font-size="16" 
        fill="#ffffff" text-anchor="middle" opacity="0.8">
    Projects that make a difference
  </text>
</svg>

</div>

### 🐚 [rad-shell](https://github.com/brandon-fryslie/rad-shell) ⭐ 41 stars

<details open>
<summary><b>Ultra-fast, feature-filled Zsh installation</b></summary>

<div align="center">

<!-- Animated Stats Bar -->
<svg width="600" height="60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="barGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="100%" style="stop-color:#00FF7F"/>
    </linearGradient>
  </defs>
  
  <text x="10" y="20" font-size="14" fill="#ffffff">⚡ Performance: </text>
  <rect x="130" y="8" width="400" height="16" fill="#1a1a1a" rx="8"/>
  <rect x="130" y="8" width="380" height="16" fill="url(#barGrad1)" rx="8">
    <animate attributeName="width" values="0;380" dur="2s" fill="freeze"/>
  </rect>
  <text x="540" y="20" font-size="14" fill="#00FF7F">95%</text>
  
  <text x="10" y="45" font-size="14" fill="#ffffff">🎨 Features: </text>
  <rect x="130" y="33" width="400" height="16" fill="#1a1a1a" rx="8"/>
  <rect x="130" y="33" width="400" height="16" fill="url(#barGrad1)" rx="8">
    <animate attributeName="width" values="0;400" dur="2s" fill="freeze"/>
  </rect>
  <text x="540" y="45" font-size="14" fill="#00FF7F">100%</text>
</svg>

</div>

A complete shell framework that thousands of developers rely on for their daily workflow. Plugin system, custom themes, blazing fast performance.

**Tech:** `Shell` `Zsh` `Terminal Automation` `DevTools`

</details>

---

### 🤖 AI & Machine Learning

<table>
<tr>
<td width="50%">

#### [macos-tts-via-openai](https://github.com/brandon-fryslie/macos-tts-via-openai)

macOS screen reader powered by OpenAI's TTS. Natural voice synthesis you could listen to all day long.

`Python` `OpenAI` `AI` `macOS`

</td>
<td width="50%">

#### [kalider](https://github.com/brandon-fryslie/kalider)

Experimental AI project pushing boundaries. *"It might not be a good idea, but it's an idea!"*

`Python` `ML/AI` `Experimental`

</td>
</tr>
</table>

---

### 🌐 Full-Stack Development

<table>
<tr>
<td width="50%">

#### [tesseract-react](https://github.com/brandon-fryslie/tesseract-react)

Modern React frontend for Tesseract project. Clean architecture, smooth UX, responsive design.

`React` `JavaScript` `Modern Web`

</td>
<td width="50%">

#### [ember-rest.coffee](https://github.com/brandon-fryslie/ember-rest.coffee) ⭐ 4

CoffeeScript REST utilities for Ember.js. Early adopter of modern JS frameworks.

`CoffeeScript` `Ember.js` `REST`

</td>
</tr>
</table>

---

### 🛠️ Developer Tools

<table>
<tr>
<td width="33%">

#### [rad-plugins](https://github.com/brandon-fryslie/rad-plugins)
Extensible plugin system. Modular architecture.

`Shell` `Plugins`

</td>
<td width="33%">

#### [handy-debugger](https://github.com/brandon-fryslie/handy-debugger)
Enhanced Node.js debugging experience.

`Node.js` `DevTools`

</td>
<td width="33%">

#### [git-taculous-zsh-theme](https://github.com/brandon-fryslie/git-taculous-zsh-theme)
Beautiful git-aware Zsh theme.

`Zsh` `Git`

</td>
</tr>
</table>

---

### 🎨 Creative Tech & IoT

<table>
<tr>
<td width="50%">

#### [esp-bloom](https://github.com/brandon-fryslie/esp-bloom)

Ambient bias lighting with ESP8266 microcontrollers. Inspired by ScreenBloom.

`Python` `ESP8266` `IoT` `Hardware`

</td>
<td width="50%">

#### [pb-sync](https://github.com/brandon-fryslie/pb-sync)

TypeScript tool for PixelBlaze LED controllers. Clean API, robust tooling.

`TypeScript` `IoT` `Hardware`

</td>
</tr>
</table>

---

<div align="center">

<!-- Animated Skills Section -->
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skillGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="100%" style="stop-color:#00FF7F"/>
    </linearGradient>
    <linearGradient id="skillGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7B68EE"/>
      <stop offset="100%" style="stop-color:#FF1493"/>
    </linearGradient>
    <linearGradient id="skillGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#FFD700"/>
      <stop offset="100%" style="stop-color:#FF8C00"/>
    </linearGradient>
  </defs>
  
  <!-- Header -->
  <text x="400" y="30" font-size="32" font-weight="bold" fill="#00D9FF" text-anchor="middle">
    💻 EXPERTISE LEVELS
  </text>
  
  <!-- Skill: Python -->
  <text x="50" y="70" font-size="18" fill="#ffffff">🐍 Python</text>
  <rect x="200" y="55" width="550" height="25" fill="#1a1a1a" rx="12"/>
  <rect x="200" y="55" width="522" height="25" fill="url(#skillGrad1)" rx="12">
    <animate attributeName="width" values="0;522" dur="1.5s" fill="freeze"/>
  </rect>
  <text x="760" y="72" font-size="16" fill="#00FF7F">95%</text>
  
  <!-- Skill: JavaScript/TypeScript -->
  <text x="50" y="115" font-size="18" fill="#ffffff">⚡ JavaScript/TS</text>
  <rect x="200" y="100" width="550" height="25" fill="#1a1a1a" rx="12"/>
  <rect x="200" y="100" width="522" height="25" fill="url(#skillGrad1)" rx="12">
    <animate attributeName="width" values="0;522" dur="1.5s" begin="0.2s" fill="freeze"/>
  </rect>
  <text x="760" y="117" font-size="16" fill="#00FF7F">95%</text>
  
  <!-- Skill: Shell/Bash -->
  <text x="50" y="160" font-size="18" fill="#ffffff">🐚 Shell/Bash</text>
  <rect x="200" y="145" width="550" height="25" fill="#1a1a1a" rx="12"/>
  <rect x="200" y="145" width="550" height="25" fill="url(#skillGrad1)" rx="12">
    <animate attributeName="width" values="0;550" dur="1.5s" begin="0.4s" fill="freeze"/>
  </rect>
  <text x="760" y="162" font-size="16" fill="#00FF7F">100%</text>
  
  <!-- Skill: React/Node -->
  <text x="50" y="205" font-size="18" fill="#ffffff">⚛️ React/Node</text>
  <rect x="200" y="190" width="550" height="25" fill="#1a1a1a" rx="12"/>
  <rect x="200" y="190" width="495" height="25" fill="url(#skillGrad2)" rx="12">
    <animate attributeName="width" values="0;495" dur="1.5s" begin="0.6s" fill="freeze"/>
  </rect>
  <text x="760" y="207" font-size="16" fill="#FF1493">90%</text>
  
  <!-- Skill: AI/ML -->
  <text x="50" y="250" font-size="18" fill="#ffffff">🤖 AI/ML</text>
  <rect x="200" y="235" width="550" height="25" fill="#1a1a1a" rx="12"/>
  <rect x="200" y="235" width="522" height="25" fill="url(#skillGrad2)" rx="12">
    <animate attributeName="width" values="0;522" dur="1.5s" begin="0.8s" fill="freeze"/>
  </rect>
  <text x="760" y="252" font-size="16" fill="#FF1493">95%</text>
  
  <!-- Skill: DevOps -->
  <text x="50" y="295" font-size="18" fill="#ffffff">🔧 DevOps</text>
  <rect x="200" y="280" width="550" height="25" fill="#1a1a1a" rx="12"/>
  <rect x="200" y="280" width="495" height="25" fill="url(#skillGrad3)" rx="12">
    <animate attributeName="width" values="0;495" dur="1.5s" begin="1s" fill="freeze"/>
  </rect>
  <text x="760" y="297" font-size="16" fill="#FF8C00">90%</text>
  
  <!-- Skill: IoT/Hardware -->
  <text x="50" y="340" font-size="18" fill="#ffffff">🎨 IoT/Hardware</text>
  <rect x="200" y="325" width="550" height="25" fill="#1a1a1a" rx="12"/>
  <rect x="200" y="325" width="495" height="25" fill="url(#skillGrad3)" rx="12">
    <animate attributeName="width" values="0;495" dur="1.5s" begin="1.2s" fill="freeze"/>
  </rect>
  <text x="760" y="342" font-size="16" fill="#FF8C00">90%</text>
  
  <!-- Animated particles -->
  <circle cx="100" cy="370" r="3" fill="#00D9FF" opacity="0.6">
    <animate attributeName="cy" values="370;350;370" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="370" r="3" fill="#FF1493" opacity="0.6">
    <animate attributeName="cy" values="370;350;370" dur="2.5s" repeatCount="indefinite"/>
  </circle>
</svg>

</div>

---

## 📊 GitHub Stats

<div align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=brandon-fryslie&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=00D9FF&icon_color=00D9FF&text_color=c9d1d9"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=brandon-fryslie&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=00D9FF&text_color=c9d1d9"/>
</div>

<div align="center">
  
[![Brandon's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=brandon-fryslie&theme=tokyo-night&hide_border=true&bg_color=0d1117&color=00D9FF&line=00D9FF&point=ffffff)](https://github.com/brandon-fryslie)

</div>

---

<div align="center">

<!-- Animated Tech Stack SVG -->
<svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="techGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="50%" style="stop-color:#7B68EE"/>
      <stop offset="100%" style="stop-color:#FF1493"/>
    </linearGradient>
  </defs>
  
  <text x="50%" y="30" font-size="28" font-weight="bold" fill="url(#techGrad)" text-anchor="middle">
    🛠️ TECH STACK
  </text>
  
  <!-- Animated tech icons -->
  <g transform="translate(50, 50)">
    <circle cx="50" cy="50" r="35" fill="#3776AB" opacity="0.8">
      <animate attributeName="r" values="35;40;35" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="50" y="58" font-size="24" text-anchor="middle">🐍</text>
    <text x="50" y="95" font-size="12" fill="#ffffff" text-anchor="middle">Python</text>
  </g>
  
  <g transform="translate(200, 50)">
    <circle cx="50" cy="50" r="35" fill="#F7DF1E" opacity="0.8">
      <animate attributeName="r" values="35;40;35" dur="2s" begin="0.2s" repeatCount="indefinite"/>
    </circle>
    <text x="50" y="58" font-size="24" text-anchor="middle">⚡</text>
    <text x="50" y="95" font-size="12" fill="#ffffff" text-anchor="middle">JavaScript</text>
  </g>
  
  <g transform="translate(350, 50)">
    <circle cx="50" cy="50" r="35" fill="#007ACC" opacity="0.8">
      <animate attributeName="r" values="35;40;35" dur="2s" begin="0.4s" repeatCount="indefinite"/>
    </circle>
    <text x="50" y="58" font-size="24" text-anchor="middle">📘</text>
    <text x="50" y="95" font-size="12" fill="#ffffff" text-anchor="middle">TypeScript</text>
  </g>
  
  <g transform="translate(500, 50)">
    <circle cx="50" cy="50" r="35" fill="#61DAFB" opacity="0.8">
      <animate attributeName="r" values="35;40;35" dur="2s" begin="0.6s" repeatCount="indefinite"/>
    </circle>
    <text x="50" y="58" font-size="24" text-anchor="middle">⚛️</text>
    <text x="50" y="95" font-size="12" fill="#ffffff" text-anchor="middle">React</text>
  </g>
  
  <g transform="translate(650, 50)">
    <circle cx="50" cy="50" r="35" fill="#43853D" opacity="0.8">
      <animate attributeName="r" values="35;40;35" dur="2s" begin="0.8s" repeatCount="indefinite"/>
    </circle>
    <text x="50" y="58" font-size="24" text-anchor="middle">🟢</text>
    <text x="50" y="95" font-size="12" fill="#ffffff" text-anchor="middle">Node.js</text>
  </g>
</svg>

### Tech Badges

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![ESP8266](https://img.shields.io/badge/ESP8266-E7352C?style=for-the-badge&logo=espressif&logoColor=white)

</div>

---

## 🌟 Philosophy & Approach

<div align="center">

<!-- Animated Philosophy SVG -->
<svg width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="glowGrad" cx="50%" cy="50%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </radialGradient>
  </defs>
  
  <!-- Central quote -->
  <circle cx="50%" cy="125" r="80" fill="url(#glowGrad)" opacity="0.3">
    <animate attributeName="r" values="80;100;80" dur="4s" repeatCount="indefinite"/>
  </circle>
  
  <text x="50%" y="115" font-size="20" font-weight="bold" fill="#00D9FF" text-anchor="middle">
    "If you're green, you're growing.
  </text>
  <text x="50%" y="140" font-size="20" font-weight="bold" fill="#00D9FF" text-anchor="middle">
    If you're ripe, you're rotten."
  </text>
  
  <!-- Orbiting values -->
  <g>
    <circle cx="50%" cy="30" r="15" fill="#00FF7F" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0 400 125" to="360 400 125" dur="10s" repeatCount="indefinite"/>
    </circle>
    <text x="50%" y="35" font-size="12" fill="#ffffff" text-anchor="middle">
      <animateTransform attributeName="transform" type="rotate" from="0 400 125" to="360 400 125" dur="10s" repeatCount="indefinite"/>
      🎯 Precision
    </text>
  </g>
  
  <g>
    <circle cx="50%" cy="220" r="15" fill="#FF1493" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="120 400 125" to="480 400 125" dur="10s" repeatCount="indefinite"/>
    </circle>
    <text x="50%" y="225" font-size="12" fill="#ffffff" text-anchor="middle">
      <animateTransform attributeName="transform" type="rotate" from="120 400 125" to="480 400 125" dur="10s" repeatCount="indefinite"/>
      🤝 Teamwork
    </text>
  </g>
  
  <g>
    <circle cx="150" cy="125" r="15" fill="#7B68EE" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="240 400 125" to="600 400 125" dur="10s" repeatCount="indefinite"/>
    </circle>
    <text x="150" y="130" font-size="12" fill="#ffffff" text-anchor="middle">
      <animateTransform attributeName="transform" type="rotate" from="240 400 125" to="600 400 125" dur="10s" repeatCount="indefinite"/>
      🌱 Growth
    </text>
  </g>
</svg>

### Core Values

🎯 **Precision** • Ship working code, iterate rapidly, solve real problems  
🤝 **Collaboration** • Team success first, clear communication, empower others  
🌱 **Growth** • Lifelong learning, stay curious, never stop improving

</div>

---

## 🎨 More Projects

<details>
<summary><b>🤖 AI & Machine Learning</b></summary>
<br>

- **[ptytest](https://github.com/brandon-fryslie/ptytest)** - Terminal emulation and PTY testing utilities
- **[kalider](https://github.com/brandon-fryslie/kalider)** - Experimental AI project
- **[macos-tts-via-openai](https://github.com/brandon-fryslie/macos-tts-via-openai)** - OpenAI-powered screen reader

</details>

<details>
<summary><b>🌐 Full-Stack Applications</b></summary>
<br>

- **[tesseract-react](https://github.com/brandon-fryslie/tesseract-react)** - Modern React frontend
- **[storyportal-web-client](https://github.com/brandon-fryslie/storyportal-web-client)** - Interactive storytelling
- **[sake](https://github.com/brandon-fryslie/sake)** - Websockets Made Easy
- **[ember-rest.coffee](https://github.com/brandon-fryslie/ember-rest.coffee)** - REST utilities for Ember.js

</details>

<details>
<summary><b>🛠️ Developer Tools</b></summary>
<br>

- **[rad-shell](https://github.com/brandon-fryslie/rad-shell)** ⭐ 41 - Ultra-fast Zsh framework
- **[rad-plugins](https://github.com/brandon-fryslie/rad-plugins)** - Plugin system
- **[git-taculous-zsh-theme](https://github.com/brandon-fryslie/git-taculous-zsh-theme)** - Git-aware theme
- **[handy-debugger](https://github.com/brandon-fryslie/handy-debugger)** - Node.js debugging
- **[dotfiles](https://github.com/brandon-fryslie/dotfiles)** - Dev environment config
- **[stacker](https://github.com/brandon-fryslie/stacker)** - Stack orchestration

</details>

<details>
<summary><b>🎨 Creative Tech & IoT</b></summary>
<br>

- **[esp-bloom](https://github.com/brandon-fryslie/esp-bloom)** - Ambient lighting with ESP8266
- **[pb-sync](https://github.com/brandon-fryslie/pb-sync)** - PixelBlaze LED controller tool

</details>

<details>
<summary><b>📚 Framework Development</b></summary>
<br>

- **[Smoke](https://github.com/brandon-fryslie/Smoke)** ⭐ 4 - CodeIgniter reinterpretation
- **[combine](https://github.com/brandon-fryslie/combine)** - Resource combination and minification

</details>

---

<div align="center">

## 💼 Open to Opportunities

<!-- Animated CTA SVG -->
<svg width="700" height="150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ctaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="100%" style="stop-color:#FF1493"/>
    </linearGradient>
  </defs>
  
  <rect x="50" y="20" width="600" height="110" rx="15" fill="none" stroke="url(#ctaGrad)" stroke-width="3">
    <animate attributeName="stroke-dasharray" values="0,2000;2000,0;0,2000" dur="4s" repeatCount="indefinite"/>
  </rect>
  
  <text x="350" y="55" font-size="22" font-weight="bold" fill="#00D9FF" text-anchor="middle">
    🚀 Interested in collaborating?
  </text>
  
  <text x="350" y="85" font-size="16" fill="#ffffff" text-anchor="middle">
    AI/ML Engineering • Senior Software Engineering
  </text>
  
  <text x="350" y="110" font-size="16" fill="#ffffff" text-anchor="middle">
    Technical Leadership • Developer Tools
  </text>
</svg>

[![GitHub](https://img.shields.io/badge/GitHub-brandon--fryslie-181717?style=for-the-badge&logo=github)](https://github.com/brandon-fryslie)
[![Profile Views](https://komarev.com/ghpvc/?username=brandon-fryslie&style=for-the-badge&color=00D9FF)](https://github.com/brandon-fryslie)

---

<!-- Animated Footer -->
<svg width="100%" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#00D9FF;#7B68EE;#FF1493;#00D9FF" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#7B68EE;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#7B68EE;#FF1493;#00D9FF;#7B68EE" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#FF1493;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#FF1493;#00D9FF;#7B68EE;#FF1493" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
  </defs>
  
  <!-- Wave animation -->
  <path d="M0,50 Q100,30 200,50 T400,50 T600,50 T800,50" stroke="url(#footerGrad)" stroke-width="3" fill="none">
    <animate attributeName="d" 
             values="M0,50 Q100,30 200,50 T400,50 T600,50 T800,50;
                     M0,50 Q100,70 200,50 T400,50 T600,50 T800,50;
                     M0,50 Q100,30 200,50 T400,50 T600,50 T800,50"
             dur="3s" repeatCount="indefinite"/>
  </path>
  
  <text x="50%" y="85" font-size="16" fill="#00D9FF" text-anchor="middle">
    "Don't take anything I say too seriously." 😉
  </text>
</svg>

**70+ repositories • 10+ years experience • Infinite curiosity**

![Hit Counter](https://hit.yhype.me/github/profile?user_id=815181)

</div>
