<div align="center">

<!-- EPIC Animated Matrix Header -->
<svg width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background: #0d1117;">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1">
        <animate attributeName="stop-color" values="#00D9FF;#7B68EE;#FF1493;#FFD700;#00D9FF" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#7B68EE;stop-opacity:1">
        <animate attributeName="stop-color" values="#7B68EE;#FF1493;#FFD700;#00D9FF;#7B68EE" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#FF1493;stop-opacity:1">
        <animate attributeName="stop-color" values="#FF1493;#FFD700;#00D9FF;#7B68EE;#FF1493" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    
    <radialGradient id="radialGlow" cx="50%" cy="50%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.8"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </radialGradient>
    
    <filter id="glow">
      <feGaussianBlur stdDeviation="5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <filter id="glow2">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Matrix Rain Effect - Multiple streams -->
  <text x="50" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.6">
    1010101<animate attributeName="y" values="-20;320" dur="3s" repeatCount="indefinite"/>
  </text>
  <text x="150" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.5">
    1100110<animate attributeName="y" values="-20;320" dur="4s" repeatCount="indefinite"/>
  </text>
  <text x="250" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.6">
    0110101<animate attributeName="y" values="-20;320" dur="3.5s" repeatCount="indefinite"/>
  </text>
  <text x="350" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.5">
    1011001<animate attributeName="y" values="-20;320" dur="4.2s" repeatCount="indefinite"/>
  </text>
  <text x="450" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.6">
    0101110<animate attributeName="y" values="-20;320" dur="3.8s" repeatCount="indefinite"/>
  </text>
  <text x="550" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.5">
    1101010<animate attributeName="y" values="-20;320" dur="4.5s" repeatCount="indefinite"/>
  </text>
  <text x="650" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.6">
    0011011<animate attributeName="y" values="-20;320" dur="3.3s" repeatCount="indefinite"/>
  </text>
  <text x="750" y="0" font-family="monospace" font-size="14" fill="#00FF41" opacity="0.5">
    1110100<animate attributeName="y" values="-20;320" dur="4.7s" repeatCount="indefinite"/>
  </text>
  
  <!-- Particle System - Floating orbs -->
  <circle cx="80" cy="100" r="3" fill="#00D9FF" opacity="0.8" filter="url(#glow2)">
    <animate attributeName="cy" values="100;50;100" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="cx" values="80;120;80" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.8;0.3;0.8" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="250" r="4" fill="#FF1493" opacity="0.7" filter="url(#glow2)">
    <animate attributeName="cy" values="250;200;250" dur="5s" repeatCount="indefinite"/>
    <animate attributeName="cx" values="200;240;200" dur="5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.7;0.3;0.7" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="80" r="3" fill="#7B68EE" opacity="0.8" filter="url(#glow2)">
    <animate attributeName="cy" values="80;120;80" dur="3.5s" repeatCount="indefinite"/>
    <animate attributeName="cx" values="700;660;700" dur="3.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.8;0.3;0.8" dur="3.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="600" cy="230" r="4" fill="#FFD700" opacity="0.7" filter="url(#glow2)">
    <animate attributeName="cy" values="230;270;230" dur="4.5s" repeatCount="indefinite"/>
    <animate attributeName="cx" values="600;640;600" dur="4.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.7;0.3;0.7" dur="4.5s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Pulsing background circles -->
  <circle cx="100" cy="100" r="40" fill="url(#radialGlow)" opacity="0.2">
    <animate attributeName="r" values="40;80;40" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.2;0.5;0.2" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="200" r="50" fill="url(#radialGlow)" opacity="0.2">
    <animate attributeName="r" values="50;90;50" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.2;0.5;0.2" dur="4s" repeatCount="indefinite"/>
  </circle>
  
  <!-- 3D Rotating Cube Wireframe -->
  <g transform="translate(400, 150)">
    <!-- Cube edges with 3D rotation effect -->
    <line x1="-40" y1="-40" x2="40" y2="-40" stroke="url(#grad1)" stroke-width="2" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="8s" repeatCount="indefinite"/>
    </line>
    <line x1="40" y1="-40" x2="40" y2="40" stroke="url(#grad1)" stroke-width="2" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="8s" repeatCount="indefinite"/>
    </line>
    <line x1="40" y1="40" x2="-40" y2="40" stroke="url(#grad1)" stroke-width="2" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="8s" repeatCount="indefinite"/>
    </line>
    <line x1="-40" y1="40" x2="-40" y2="-40" stroke="url(#grad1)" stroke-width="2" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="8s" repeatCount="indefinite"/>
    </line>
    
    <!-- Inner rotating ring -->
    <circle cx="0" cy="0" r="60" fill="none" stroke="url(#grad1)" stroke-width="2" opacity="0.4">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="6s" repeatCount="indefinite"/>
    </circle>
  </g>
  
  <!-- Main Title with extreme glow -->
  <text x="50%" y="130" font-family="'Courier New', monospace" font-size="56" font-weight="bold" 
        fill="url(#grad1)" text-anchor="middle" filter="url(#glow)">
    BRANDON FRYSLIE
    <animate attributeName="opacity" values="1;0.8;1" dur="2s" repeatCount="indefinite"/>
  </text>
  
  <text x="50%" y="170" font-family="'Courier New', monospace" font-size="22" 
        fill="#00D9FF" text-anchor="middle" filter="url(#glow2)">
    <tspan>Senior Software Engineer • AI/ML • Open Source</tspan>
    <animate attributeName="opacity" values="0.9;1;0.9" dur="3s" repeatCount="indefinite"/>
  </text>
  
  <!-- Animated scanning line -->
  <line x1="0" y1="180" x2="100%" y2="180" stroke="#00D9FF" stroke-width="2" opacity="0.6">
    <animate attributeName="y1" values="0;300;0" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="y2" values="0;300;0" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0.2;0.6" dur="4s" repeatCount="indefinite"/>
  </line>
  
  <!-- Hexagon pattern -->
  <polygon points="400,220 420,232 420,256 400,268 380,256 380,232" fill="none" stroke="url(#grad1)" stroke-width="2" opacity="0.5">
    <animateTransform attributeName="transform" type="rotate" from="0 400 244" to="360 400 244" dur="10s" repeatCount="indefinite"/>
  </polygon>
  <polygon points="400,220 420,232 420,256 400,268 380,256 380,232" fill="none" stroke="url(#grad1)" stroke-width="2" opacity="0.5">
    <animateTransform attributeName="transform" type="rotate" from="360 400 244" to="0 400 244" dur="7s" repeatCount="indefinite"/>
    <animateTransform attributeName="transform" type="scale" from="1" to="1.5" additive="sum" dur="3s" repeatCount="indefinite"/>
  </polygon>
</svg>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=2000&pause=500&color=00D9FF&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=100&lines=%F0%9F%9A%80+Building+the+future%2C+one+commit+at+a+time;%F0%9F%A7%A0+AI%2FML+%7C+%E2%9A%A1+Full-Stack+%7C+%F0%9F%90%9A+DevTools;70%2B+repositories+%7C+10%2B+years+experience+%7C+%E2%88%9E+curiosity;%22Stay+green%2C+keep+growing%22+%F0%9F%8C%B1)](https://git.io/typing-svg)

[![GitHub followers](https://img.shields.io/github/followers/brandon-fryslie?style=for-the-badge&logo=github&color=00D9FF&labelColor=0d1117)](https://github.com/brandon-fryslie)
[![Profile Views](https://komarev.com/ghpvc/?username=brandon-fryslie&style=for-the-badge&color=00D9FF&labelColor=0d1117)](https://github.com/brandon-fryslie)

</div>

---

## 🚀 About Me

```javascript
const brandon = {
    status: "🔥 Currently: Crushing it in AI/ML & DevTools",
    location: "🌎 Earth // 🚀 The Future",
    languages: ["Python", "JavaScript", "TypeScript", "Shell", "PHP", "CoffeeScript"],
    expertise: {
        ai_ml: ["OpenAI APIs", "LLMs", "TTS/STT", "AI Integration", "Prompt Engineering"],
        fullstack: ["React", "Node.js", "Express", "REST APIs", "WebSockets", "Real-time"],
        devtools: ["CLI Tools", "Zsh Framework", "Terminal Magic", "Dev Experience"],
        devops: ["Docker", "CI/CD", "Automation", "Infrastructure as Code"],
        creative: ["IoT", "ESP8266", "LED Programming", "Hardware Hacking"]
    },
    currentFocus: "🤖 AI-powered developer tools that blow minds",
    philosophy: "If you're green, you're growing. If you're ripe, you're rotten. 🌱",
    superpower: "Turning complex problems into elegant solutions ✨",
    funFact: "Built a Zsh framework used by thousands of developers worldwide! 🎯"
};
```

<div align="center">

<!-- Mega Animated Divider with Particles -->
<svg width="100%" height="60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1">
        <animate attributeName="offset" values="-0.5;1.5" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#7B68EE;stop-opacity:1">
        <animate attributeName="offset" values="0;2" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#FF1493;stop-opacity:1">
        <animate attributeName="offset" values="0.5;2.5" dur="3s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
  </defs>
  <rect width="100%" height="4" fill="url(#lineGrad)" y="28"/>
  
  <!-- Mini particles -->
  <circle cx="10%" cy="30" r="2" fill="#00D9FF" opacity="0.6">
    <animate attributeName="cx" values="10%;90%;10%" dur="8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="90%" cy="30" r="2" fill="#FF1493" opacity="0.6">
    <animate attributeName="cx" values="90%;10%;90%" dur="10s" repeatCount="indefinite"/>
  </circle>
</svg>

</div>

---

## 🔥 Featured Projects

<div align="center">

<!-- INSANE Animated Project Showcase -->
<svg width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="projectGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#00D9FF;#FF1493;#FFD700;#00D9FF" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#7B68EE;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#7B68EE;#00D9FF;#FF1493;#7B68EE" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    
    <filter id="projectGlow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- 3D Hexagon particles -->
  <g opacity="0.7">
    <polygon points="100,30 120,42 120,66 100,78 80,66 80,42" fill="url(#projectGrad)">
      <animateTransform attributeName="transform" type="rotate" from="0 100 54" to="360 100 54" dur="10s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0.3;0.7" dur="3s" repeatCount="indefinite"/>
    </polygon>
  </g>
  
  <g opacity="0.6">
    <polygon points="200,90 220,102 220,126 200,138 180,126 180,102" fill="url(#projectGrad)">
      <animateTransform attributeName="transform" type="rotate" from="360 200 114" to="0 200 114" dur="8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0.3;0.6" dur="4s" repeatCount="indefinite"/>
    </polygon>
  </g>
  
  <!-- Pulsing stars -->
  <circle cx="700" cy="40" r="3" fill="#FFD700" filter="url(#projectGlow)">
    <animate attributeName="r" values="3;6;3" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="650" cy="110" r="2" fill="#00D9FF" filter="url(#projectGlow)">
    <animate attributeName="r" values="2;5;2" dur="2s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Main text -->
  <text x="50%" y="70" font-family="Arial, sans-serif" font-size="36" font-weight="bold" 
        fill="url(#projectGrad)" text-anchor="middle" filter="url(#projectGlow)">
    🚀 EPIC PROJECTS 🚀
  </text>
  
  <text x="50%" y="105" font-family="Arial, sans-serif" font-size="18" 
        fill="#ffffff" text-anchor="middle" opacity="0.9">
    Projects that make developers' lives better
    <animate attributeName="opacity" values="0.9;0.6;0.9" dur="2s" repeatCount="indefinite"/>
  </text>
  
  <!-- Animated arrows -->
  <text x="30%" y="70" font-size="30" fill="#00D9FF" opacity="0.6">
    ⟩<animate attributeName="x" values="25%;30%;25%" dur="2s" repeatCount="indefinite"/>
  </text>
  <text x="70%" y="70" font-size="30" fill="#FF1493" opacity="0.6">
    ⟨<animate attributeName="x" values="70%;65%;70%" dur="2s" repeatCount="indefinite"/>
  </text>
</svg>

</div>

### 🐚 [rad-shell](https://github.com/brandon-fryslie/rad-shell) ⭐ 41 stars

<details open>
<summary><b>⚡ Ultra-fast, feature-filled Zsh installation framework</b></summary>

<div align="center">

<!-- MEGA Animated Stats Bars with Particles -->
<svg width="700" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="barGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="50%" style="stop-color:#00FF7F"/>
      <stop offset="100%" style="stop-color:#FFD700"/>
    </linearGradient>
    <linearGradient id="barGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#FF1493"/>
      <stop offset="50%" style="stop-color:#7B68EE"/>
      <stop offset="100%" style="stop-color:#00D9FF"/>
    </linearGradient>
    <filter id="barGlow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Performance bar -->
  <text x="10" y="25" font-size="16" fill="#ffffff" font-weight="bold">⚡ Performance:</text>
  <rect x="160" y="12" width="480" height="20" fill="#1a1a1a" rx="10" stroke="#00D9FF" stroke-width="1"/>
  <rect x="160" y="12" width="456" height="20" fill="url(#barGrad1)" rx="10" filter="url(#barGlow)">
    <animate attributeName="width" values="0;456" dur="2s" fill="freeze"/>
  </rect>
  <text x="655" y="25" font-size="16" fill="#00FF7F" font-weight="bold">95%</text>
  
  <!-- Sparkle particles -->
  <circle cx="200" cy="22" r="2" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.5s" dur="0.5s"/>
  </circle>
  <circle cx="400" cy="22" r="2" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.8s" dur="0.5s"/>
  </circle>
  <circle cx="600" cy="22" r="2" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.1s" dur="0.5s"/>
  </circle>
  
  <!-- Features bar -->
  <text x="10" y="65" font-size="16" fill="#ffffff" font-weight="bold">🎨 Features:</text>
  <rect x="160" y="52" width="480" height="20" fill="#1a1a1a" rx="10" stroke="#FF1493" stroke-width="1"/>
  <rect x="160" y="52" width="480" height="20" fill="url(#barGrad2)" rx="10" filter="url(#barGlow)">
    <animate attributeName="width" values="0;480" dur="2s" fill="freeze"/>
  </rect>
  <text x="655" y="65" font-size="16" fill="#FF1493" font-weight="bold">100%</text>
  
  <!-- Sparkle particles for features -->
  <circle cx="200" cy="62" r="2" fill="#7B68EE" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.5s" dur="0.5s"/>
  </circle>
  <circle cx="400" cy="62" r="2" fill="#7B68EE" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.8s" dur="0.5s"/>
  </circle>
  <circle cx="600" cy="62" r="2" fill="#7B68EE" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.1s" dur="0.5s"/>
  </circle>
  
  <!-- Stats display -->
  <text x="350" y="100" font-size="14" fill="#00D9FF" text-anchor="middle">
    📦 41 Stars • 🍴 7 Forks • 🔥 Thousands of Users
  </text>
</svg>

</div>

A complete shell framework that revolutionizes terminal productivity. Plugin system, custom themes, blazing fast performance, and loved by developers worldwide.

**Tech Stack:** `Shell` `Zsh` `Terminal Automation` `Developer Experience` `Productivity Tools`

**Key Features:** ⚡ Lightning-fast startup • 🔌 Extensible plugins • 🎨 Beautiful themes • 📦 Easy installation

</details>

---

### 🤖 AI & Machine Learning Projects

<table>
<tr>
<td width="50%">

#### 🗣️ [macos-tts-via-openai](https://github.com/brandon-fryslie/macos-tts-via-openai)

**OpenAI-Powered Screen Reader** - Natural voice synthesis you could listen to all day. Brings high-quality AI voices to macOS accessibility.

`Python` `OpenAI API` `TTS` `macOS` `Accessibility` `AI`

**Features:** 🎙️ Natural voices • 🔄 Real-time processing • 🎯 macOS integration

</td>
<td width="50%">

#### 🧪 [kalider](https://github.com/brandon-fryslie/kalider)

**Experimental AI Project** - Pushing the boundaries of what's possible. *"It might not be a good idea, but it's an idea!"*

`Python` `Machine Learning` `AI` `Experimental`

**Status:** 🚧 Active development • 🔬 R&D phase • 💡 Innovative approaches

</td>
</tr>
<tr>
<td width="50%">

#### 🖥️ [ptytest](https://github.com/brandon-fryslie/ptytest)

**Terminal Emulation Toolkit** - PTY testing utilities for building robust CLI applications. Essential for terminal app development.

`Python` `PTY` `Terminal` `Testing` `CLI`

**Use Cases:** 🧪 CLI testing • 🔧 Terminal debugging • 📦 Dev tools

</td>
<td width="50%">

<div align="center">

<!-- AI Stats SVG -->
<svg width="100%" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="aiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="100%" style="stop-color:#FF1493"/>
    </linearGradient>
  </defs>
  
  <text x="50%" y="30" font-size="20" fill="url(#aiGrad)" text-anchor="middle" font-weight="bold">
    🧠 AI/ML Focus Areas
  </text>
  
  <text x="50%" y="60" font-size="14" fill="#ffffff" text-anchor="middle">
    🤖 LLM Integration
  </text>
  <text x="50%" y="80" font-size="14" fill="#ffffff" text-anchor="middle">
    🗣️ Speech Synthesis
  </text>
  <text x="50%" y="100" font-size="14" fill="#ffffff" text-anchor="middle">
    ⚡ Real-time AI
  </text>
  
  <!-- Animated AI brain -->
  <circle cx="50%" cy="35" r="30" fill="none" stroke="url(#aiGrad)" stroke-width="2" opacity="0.3">
    <animate attributeName="r" values="30;35;30" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>

</div>

</td>
</tr>
</table>

---

### 🌐 Full-Stack Web Applications

<table>
<tr>
<td width="50%">

#### ⚛️ [tesseract-react](https://github.com/brandon-fryslie/tesseract-react)

**Modern React Frontend** - Clean architecture, smooth UX, responsive design. Built for scale and maintainability.

`React` `JavaScript` `Modern Web` `SPA`

</td>
<td width="50%">

#### 📱 [storyportal-web-client](https://github.com/brandon-fryslie/storyportal-web-client)

**Interactive Storytelling Platform** - Engaging web experience for digital narratives.

`JavaScript` `Web APIs` `Interactive`

</td>
</tr>
<tr>
<td width="50%">

#### ☕ [ember-rest.coffee](https://github.com/brandon-fryslie/ember-rest.coffee) ⭐ 4

**Ember.js REST Utilities** - CoffeeScript port of essential REST functions. Early adopter of modern JS frameworks.

`CoffeeScript` `Ember.js` `REST APIs`

</td>
<td width="50%">

#### 🌐 [sake](https://github.com/brandon-fryslie/sake)

**Websockets Made Easy** - Clean abstractions for real-time communication. Simplifying the complex.

`CoffeeScript` `WebSockets` `Real-time`

</td>
</tr>
</table>

---

### 🛠️ Developer Tools Arsenal

<table>
<tr>
<td width="33%">

#### 🔌 [rad-plugins](https://github.com/brandon-fryslie/rad-plugins)

**Plugin System** - Extensible architecture for rad-shell. Modular, clean, powerful.

`Shell` `Plugins` `Architecture`

</td>
<td width="33%">

#### 🐛 [handy-debugger](https://github.com/brandon-fryslie/handy-debugger)

**Node.js Debugging** - Enhanced developer experience for debugging.

`Node.js` `JavaScript` `DevTools`

</td>
<td width="33%">

#### 🎨 [git-taculous-zsh-theme](https://github.com/brandon-fryslie/git-taculous-zsh-theme)

**Zsh Theme** - Beautiful git-aware terminal theme. Fast and gorgeous.

`Zsh` `Git` `Theme`

</td>
</tr>
<tr>
<td width="33%">

#### 📦 [stacker](https://github.com/brandon-fryslie/stacker)

**Stack Orchestration** - Boot your stack with ease. Dev environment management.

`CoffeeScript` `DevOps`

</td>
<td width="33%">

#### ⚙️ [dotfiles](https://github.com/brandon-fryslie/dotfiles)

**Dev Environment** - Personal configuration that powers productivity.

`Shell` `Config` `Dotfiles`

</td>
<td width="33%">

#### 🎯 [sublime-profile](https://github.com/brandon-fryslie/sublime-profile)

**Editor Config** - Sublime Text customizations for optimal coding.

`Python` `Editor` `Config`

</td>
</tr>
</table>

---

### 🎨 Creative Tech & IoT

<table>
<tr>
<td width="50%">

#### 💡 [esp-bloom](https://github.com/brandon-fryslie/esp-bloom)

**Ambient Bias Lighting** - ESP8266 microcontroller-based lighting system. Inspired by ScreenBloom, enhanced with custom features.

`Python` `ESP8266` `IoT` `Hardware` `LED`

**Features:** 🌈 Dynamic colors • 📺 Screen sync • 🎮 Custom patterns

</td>
<td width="50%">

#### 🎆 [pb-sync](https://github.com/brandon-fryslie/pb-sync)

**PixelBlaze Integration** - TypeScript tool for LED controller interaction. Clean API, robust tooling.

`TypeScript` `IoT` `Hardware` `LED` `API`

**Capabilities:** 🔌 Hardware control • 🎨 Pattern sync • 📡 Remote management

</td>
</tr>
</table>

---

<div align="center">

<!-- MEGA SKILLS SECTION with INSANE Animations -->
<svg width="900" height="550" xmlns="http://www.w3.org/2000/svg">
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
    <radialGradient id="skillGlow">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.5"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </radialGradient>
    <filter id="skillFilter">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Rotating background elements -->
  <circle cx="100" cy="100" r="50" fill="url(#skillGlow)">
    <animate attributeName="r" values="50;80;50" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="800" cy="450" r="60" fill="url(#skillGlow)">
    <animate attributeName="r" values="60;90;60" dur="5s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Matrix particles -->
  <text x="50" y="0" font-family="monospace" font-size="10" fill="#00FF41" opacity="0.3">
    AI<animate attributeName="y" values="-20;570" dur="6s" repeatCount="indefinite"/>
  </text>
  <text x="850" y="0" font-family="monospace" font-size="10" fill="#00FF41" opacity="0.3">
    ML<animate attributeName="y" values="-20;570" dur="7s" repeatCount="indefinite"/>
  </text>
  
  <!-- Header -->
  <text x="450" y="50" font-size="40" font-weight="bold" fill="url(#skillGrad1)" text-anchor="middle" filter="url(#skillFilter)">
    💻 EXPERTISE MATRIX
  </text>
  
  <!-- Skill 1: Python -->
  <text x="80" y="110" font-size="20" fill="#ffffff" font-weight="bold">🐍 Python</text>
  <rect x="250" y="92" width="600" height="30" fill="#1a1a1a" rx="15" stroke="#00D9FF" stroke-width="2"/>
  <rect x="250" y="92" width="570" height="30" fill="url(#skillGrad1)" rx="15" filter="url(#skillFilter)">
    <animate attributeName="width" values="0;570" dur="1.8s" fill="freeze"/>
  </rect>
  <text x="865" y="112" font-size="18" fill="#00FF7F" font-weight="bold">95%</text>
  <!-- Sparkles -->
  <circle cx="300" cy="107" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.5s" dur="0.3s"/>
  </circle>
  <circle cx="600" cy="107" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.7s" dur="0.3s"/>
  </circle>
  
  <!-- Skill 2: JavaScript/TypeScript -->
  <text x="80" y="170" font-size="20" fill="#ffffff" font-weight="bold">⚡ JS/TypeScript</text>
  <rect x="250" y="152" width="600" height="30" fill="#1a1a1a" rx="15" stroke="#00D9FF" stroke-width="2"/>
  <rect x="250" y="152" width="570" height="30" fill="url(#skillGrad1)" rx="15" filter="url(#skillFilter)">
    <animate attributeName="width" values="0;570" dur="1.8s" begin="0.2s" fill="freeze"/>
  </rect>
  <text x="865" y="172" font-size="18" fill="#00FF7F" font-weight="bold">95%</text>
  <circle cx="300" cy="167" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.7s" dur="0.3s"/>
  </circle>
  <circle cx="600" cy="167" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.9s" dur="0.3s"/>
  </circle>
  
  <!-- Skill 3: Shell/Bash -->
  <text x="80" y="230" font-size="20" fill="#ffffff" font-weight="bold">🐚 Shell/Bash</text>
  <rect x="250" y="212" width="600" height="30" fill="#1a1a1a" rx="15" stroke="#00FF7F" stroke-width="2"/>
  <rect x="250" y="212" width="600" height="30" fill="url(#skillGrad1)" rx="15" filter="url(#skillFilter)">
    <animate attributeName="width" values="0;600" dur="1.8s" begin="0.4s" fill="freeze"/>
  </rect>
  <text x="865" y="232" font-size="18" fill="#00FF7F" font-weight="bold">100%</text>
  <circle cx="300" cy="227" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="1.9s" dur="0.3s"/>
  </circle>
  <circle cx="600" cy="227" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.1s" dur="0.3s"/>
  </circle>
  <circle cx="820" cy="227" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.2s" dur="0.3s"/>
  </circle>
  
  <!-- Skill 4: React/Node -->
  <text x="80" y="290" font-size="20" fill="#ffffff" font-weight="bold">⚛️ React/Node</text>
  <rect x="250" y="272" width="600" height="30" fill="#1a1a1a" rx="15" stroke="#FF1493" stroke-width="2"/>
  <rect x="250" y="272" width="540" height="30" fill="url(#skillGrad2)" rx="15" filter="url(#skillFilter)">
    <animate attributeName="width" values="0;540" dur="1.8s" begin="0.6s" fill="freeze"/>
  </rect>
  <text x="865" y="292" font-size="18" fill="#FF1493" font-weight="bold">90%</text>
  <circle cx="300" cy="287" r="3" fill="#7B68EE" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.1s" dur="0.3s"/>
  </circle>
  <circle cx="600" cy="287" r="3" fill="#7B68EE" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.3s" dur="0.3s"/>
  </circle>
  
  <!-- Skill 5: AI/ML -->
  <text x="80" y="350" font-size="20" fill="#ffffff" font-weight="bold">🤖 AI/ML</text>
  <rect x="250" y="332" width="600" height="30" fill="#1a1a1a" rx="15" stroke="#7B68EE" stroke-width="2"/>
  <rect x="250" y="332" width="570" height="30" fill="url(#skillGrad2)" rx="15" filter="url(#skillFilter)">
    <animate attributeName="width" values="0;570" dur="1.8s" begin="0.8s" fill="freeze"/>
  </rect>
  <text x="865" y="352" font-size="18" fill="#FF1493" font-weight="bold">95%</text>
  <circle cx="300" cy="347" r="3" fill="#7B68EE" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.3s" dur="0.3s"/>
  </circle>
  <circle cx="600" cy="347" r="3" fill="#7B68EE" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.5s" dur="0.3s"/>
  </circle>
  
  <!-- Skill 6: DevOps -->
  <text x="80" y="410" font-size="20" fill="#ffffff" font-weight="bold">🔧 DevOps</text>
  <rect x="250" y="392" width="600" height="30" fill="#1a1a1a" rx="15" stroke="#FFD700" stroke-width="2"/>
  <rect x="250" y="392" width="540" height="30" fill="url(#skillGrad3)" rx="15" filter="url(#skillFilter)">
    <animate attributeName="width" values="0;540" dur="1.8s" begin="1s" fill="freeze"/>
  </rect>
  <text x="865" y="412" font-size="18" fill="#FF8C00" font-weight="bold">90%</text>
  <circle cx="300" cy="407" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.5s" dur="0.3s"/>
  </circle>
  <circle cx="600" cy="407" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.7s" dur="0.3s"/>
  </circle>
  
  <!-- Skill 7: IoT/Hardware -->
  <text x="80" y="470" font-size="20" fill="#ffffff" font-weight="bold">🎨 IoT/Hardware</text>
  <rect x="250" y="452" width="600" height="30" fill="#1a1a1a" rx="15" stroke="#FF8C00" stroke-width="2"/>
  <rect x="250" y="452" width="540" height="30" fill="url(#skillGrad3)" rx="15" filter="url(#skillFilter)">
    <animate attributeName="width" values="0;540" dur="1.8s" begin="1.2s" fill="freeze"/>
  </rect>
  <text x="865" y="472" font-size="18" fill="#FF8C00" font-weight="bold">90%</text>
  <circle cx="300" cy="467" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.7s" dur="0.3s"/>
  </circle>
  <circle cx="600" cy="467" r="3" fill="#FFD700" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="2.9s" dur="0.3s"/>
  </circle>
  
  <!-- Summary stats -->
  <text x="450" y="520" font-size="16" fill="#00D9FF" text-anchor="middle">
    📊 7 Core Competencies • 🚀 10+ Years Experience • ⭐ 70+ Repositories
  </text>
</svg>

</div>

---

## 📊 GitHub Stats

<div align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=brandon-fryslie&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=00D9FF&icon_color=00D9FF&text_color=c9d1d9&ring_color=FF1493&fire_color=FFD700"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=brandon-fryslie&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=00D9FF&text_color=c9d1d9"/>
</div>

<div align="center">
  
[![Brandon's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=brandon-fryslie&theme=tokyo-night&hide_border=true&bg_color=0d1117&color=00D9FF&line=FF1493&point=FFD700)](https://github.com/brandon-fryslie)

</div>

---

<div align="center">

<!-- INSANE Animated Tech Stack with 3D effects -->
<svg width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="techGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF">
        <animate attributeName="stop-color" values="#00D9FF;#FF1493;#FFD700;#00D9FF" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#7B68EE">
        <animate attributeName="stop-color" values="#7B68EE;#00D9FF;#FF1493;#7B68EE" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#FF1493">
        <animate attributeName="stop-color" values="#FF1493;#FFD700;#00D9FF;#FF1493" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    
    <filter id="techGlow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <text x="50%" y="40" font-size="32" font-weight="bold" fill="url(#techGrad)" text-anchor="middle" filter="url(#techGlow)">
    🛠️ TECH ARSENAL
  </text>
  
  <!-- Animated tech icons with 3D pulsing effect -->
  <g transform="translate(80, 80)">
    <circle cx="0" cy="0" r="40" fill="#3776AB" opacity="0.8" filter="url(#techGlow)">
      <animate attributeName="r" values="40;50;40" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="35" fill="none" stroke="#00D9FF" stroke-width="2">
      <animate attributeName="r" values="35;45;35" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="10" font-size="32" text-anchor="middle">🐍</text>
    <text x="0" y="70" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">Python</text>
  </g>
  
  <g transform="translate(230, 80)">
    <circle cx="0" cy="0" r="40" fill="#F7DF1E" opacity="0.8" filter="url(#techGlow)">
      <animate attributeName="r" values="40;50;40" dur="2s" begin="0.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" begin="0.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="35" fill="none" stroke="#FFD700" stroke-width="2">
      <animate attributeName="r" values="35;45;35" dur="2s" begin="0.2s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="10" font-size="32" text-anchor="middle">⚡</text>
    <text x="0" y="70" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">JavaScript</text>
  </g>
  
  <g transform="translate(380, 80)">
    <circle cx="0" cy="0" r="40" fill="#007ACC" opacity="0.8" filter="url(#techGlow)">
      <animate attributeName="r" values="40;50;40" dur="2s" begin="0.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" begin="0.4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="35" fill="none" stroke="#007ACC" stroke-width="2">
      <animate attributeName="r" values="35;45;35" dur="2s" begin="0.4s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="10" font-size="32" text-anchor="middle">📘</text>
    <text x="0" y="70" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">TypeScript</text>
  </g>
  
  <g transform="translate(530, 80)">
    <circle cx="0" cy="0" r="40" fill="#61DAFB" opacity="0.8" filter="url(#techGlow)">
      <animate attributeName="r" values="40;50;40" dur="2s" begin="0.6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" begin="0.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="35" fill="none" stroke="#61DAFB" stroke-width="2">
      <animate attributeName="r" values="35;45;35" dur="2s" begin="0.6s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="10" font-size="32" text-anchor="middle">⚛️</text>
    <text x="0" y="70" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">React</text>
  </g>
  
  <g transform="translate(680, 80)">
    <circle cx="0" cy="0" r="40" fill="#43853D" opacity="0.8" filter="url(#techGlow)">
      <animate attributeName="r" values="40;50;40" dur="2s" begin="0.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" begin="0.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="35" fill="none" stroke="#00FF7F" stroke-width="2">
      <animate attributeName="r" values="35;45;35" dur="2s" begin="0.8s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="10" font-size="32" text-anchor="middle">🟢</text>
    <text x="0" y="70" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">Node.js</text>
  </g>
  
  <!-- Connecting lines with animation -->
  <line x1="120" y1="80" x2="190" y2="80" stroke="url(#techGrad)" stroke-width="2" opacity="0.5">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
  </line>
  <line x1="270" y1="80" x2="340" y2="80" stroke="url(#techGrad)" stroke-width="2" opacity="0.5">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" begin="0.2s" repeatCount="indefinite"/>
  </line>
  <line x1="420" y1="80" x2="490" y2="80" stroke="url(#techGrad)" stroke-width="2" opacity="0.5">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" begin="0.4s" repeatCount="indefinite"/>
  </line>
  <line x1="570" y1="80" x2="640" y2="80" stroke="url(#techGrad)" stroke-width="2" opacity="0.5">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" begin="0.6s" repeatCount="indefinite"/>
  </line>
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

<!-- Epic Philosophy SVG with Orbiting Elements -->
<svg width="100%" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="glowGrad" cx="50%" cy="50%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.8"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </radialGradient>
    
    <linearGradient id="quoteGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="50%" style="stop-color:#7B68EE"/>
      <stop offset="100%" style="stop-color:#FF1493"/>
    </linearGradient>
    
    <filter id="quoteGlow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Central pulsing glow -->
  <circle cx="50%" cy="150" r="100" fill="url(#glowGrad)" opacity="0.3">
    <animate attributeName="r" values="100;140;100" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.3;0.6;0.3" dur="4s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Quote -->
  <text x="50%" y="135" font-size="24" font-weight="bold" fill="url(#quoteGrad)" text-anchor="middle" filter="url(#quoteGlow)">
    "If you're green, you're growing. 🌱
  </text>
  <text x="50%" y="165" font-size="24" font-weight="bold" fill="url(#quoteGrad)" text-anchor="middle" filter="url(#quoteGlow)">
    If you're ripe, you're rotten."
  </text>
  
  <!-- Orbiting value 1: Precision -->
  <g>
    <circle cx="50%" cy="30" r="20" fill="#00FF7F" opacity="0.8" filter="url(#quoteGlow)">
      <animateTransform attributeName="transform" type="rotate" from="0 450 150" to="360 450 150" dur="10s" repeatCount="indefinite"/>
      <animate attributeName="r" values="20;25;20" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="50%" y="37" font-size="14" fill="#000000" text-anchor="middle" font-weight="bold">
      <animateTransform attributeName="transform" type="rotate" from="0 450 150" to="360 450 150" dur="10s" repeatCount="indefinite"/>
      🎯
    </text>
    <text x="50%" y="70" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">
      <animateTransform attributeName="transform" type="rotate" from="0 450 150" to="360 450 150" dur="10s" repeatCount="indefinite"/>
      Precision
    </text>
  </g>
  
  <!-- Orbiting value 2: Teamwork -->
  <g>
    <circle cx="50%" cy="270" r="20" fill="#FF1493" opacity="0.8" filter="url(#quoteGlow)">
      <animateTransform attributeName="transform" type="rotate" from="120 450 150" to="480 450 150" dur="10s" repeatCount="indefinite"/>
      <animate attributeName="r" values="20;25;20" dur="2s" begin="0.7s" repeatCount="indefinite"/>
    </circle>
    <text x="50%" y="277" font-size="14" fill="#000000" text-anchor="middle" font-weight="bold">
      <animateTransform attributeName="transform" type="rotate" from="120 450 150" to="480 450 150" dur="10s" repeatCount="indefinite"/>
      🤝
    </text>
    <text x="50%" y="310" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">
      <animateTransform attributeName="transform" type="rotate" from="120 450 150" to="480 450 150" dur="10s" repeatCount="indefinite"/>
      Teamwork
    </text>
  </g>
  
  <!-- Orbiting value 3: Growth -->
  <g>
    <circle cx="200" cy="150" r="20" fill="#7B68EE" opacity="0.8" filter="url(#quoteGlow)">
      <animateTransform attributeName="transform" type="rotate" from="240 450 150" to="600 450 150" dur="10s" repeatCount="indefinite"/>
      <animate attributeName="r" values="20;25;20" dur="2s" begin="1.4s" repeatCount="indefinite"/>
    </circle>
    <text x="200" y="157" font-size="14" fill="#000000" text-anchor="middle" font-weight="bold">
      <animateTransform attributeName="transform" type="rotate" from="240 450 150" to="600 450 150" dur="10s" repeatCount="indefinite"/>
      🌱
    </text>
    <text x="200" y="190" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold">
      <animateTransform attributeName="transform" type="rotate" from="240 450 150" to="600 450 150" dur="10s" repeatCount="indefinite"/>
      Growth
    </text>
  </g>
  
  <!-- Orbit path visualization -->
  <circle cx="50%" cy="150" r="120" fill="none" stroke="#00D9FF" stroke-width="1" opacity="0.2" stroke-dasharray="5,5">
    <animate attributeName="stroke-dashoffset" values="0;-10" dur="1s" repeatCount="indefinite"/>
  </circle>
</svg>

### Core Values

**🎯 Precision** • Ship working code • Iterate rapidly • Solve real problems  
**🤝 Collaboration** • Team success first • Clear communication • Empower others  
**🌱 Growth** • Lifelong learning • Stay curious • Never stop improving

</div>

---

## 🎨 More Projects

<details>
<summary><b>🤖 AI & Machine Learning</b></summary>
<br>

- **[ptytest](https://github.com/brandon-fryslie/ptytest)** - Terminal emulation and PTY testing utilities for robust CLI apps
- **[kalider](https://github.com/brandon-fryslie/kalider)** - Experimental AI project pushing boundaries  
- **[macos-tts-via-openai](https://github.com/brandon-fryslie/macos-tts-via-openai)** - OpenAI-powered natural voice screen reader

</details>

<details>
<summary><b>🌐 Full-Stack Applications</b></summary>
<br>

- **[tesseract-react](https://github.com/brandon-fryslie/tesseract-react)** - Modern React frontend with clean architecture
- **[storyportal-web-client](https://github.com/brandon-fryslie/storyportal-web-client)** - Interactive web storytelling platform
- **[sake](https://github.com/brandon-fryslie/sake)** - Websockets Made Easy - clean real-time abstractions
- **[ember-rest.coffee](https://github.com/brandon-fryslie/ember-rest.coffee)** ⭐ 4 - REST utilities for Ember.js

</details>

<details>
<summary><b>🛠️ Developer Tools</b></summary>
<br>

- **[rad-shell](https://github.com/brandon-fryslie/rad-shell)** ⭐ 41 - Ultra-fast Zsh installation framework
- **[rad-plugins](https://github.com/brandon-fryslie/rad-plugins)** - Extensible plugin system for rad-shell
- **[git-taculous-zsh-theme](https://github.com/brandon-fryslie/git-taculous-zsh-theme)** - Beautiful git-aware Zsh theme
- **[handy-debugger](https://github.com/brandon-fryslie/handy-debugger)** - Enhanced Node.js debugging experience
- **[dotfiles](https://github.com/brandon-fryslie/dotfiles)** - Personal development environment configuration
- **[stacker](https://github.com/brandon-fryslie/stacker)** - Boot your stack - container orchestration made easy
- **[sublime-profile](https://github.com/brandon-fryslie/sublime-profile)** - Sublime Text customizations

</details>

<details>
<summary><b>🎨 Creative Tech & IoT</b></summary>
<br>

- **[esp-bloom](https://github.com/brandon-fryslie/esp-bloom)** - Ambient bias lighting with ESP8266 microcontrollers
- **[pb-sync](https://github.com/brandon-fryslie/pb-sync)** - TypeScript tool for PixelBlaze LED controller integration

</details>

<details>
<summary><b>📚 Framework Development</b></summary>
<br>

- **[Smoke](https://github.com/brandon-fryslie/Smoke)** ⭐ 4 - Reinterpretation of CodeIgniter 2.0.2 demonstrating framework expertise
- **[combine](https://github.com/brandon-fryslie/combine)** - PHP script to combine and minify resources

</details>

---

<div align="center">

## 💼 Open to Opportunities

<!-- Epic CTA with Advanced Animations -->
<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ctaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00D9FF">
        <animate attributeName="stop-color" values="#00D9FF;#FF1493;#FFD700;#00D9FF" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#FF1493">
        <animate attributeName="stop-color" values="#FF1493;#FFD700;#00D9FF;#FF1493" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    
    <filter id="ctaGlow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMergeNode>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Animated border -->
  <rect x="50" y="30" width="700" height="140" rx="20" fill="none" stroke="url(#ctaGrad)" stroke-width="4" filter="url(#ctaGlow)">
    <animate attributeName="stroke-dasharray" values="0,2800;2800,0;0,2800" dur="6s" repeatCount="indefinite"/>
  </rect>
  
  <!-- Corner decorations -->
  <circle cx="70" cy="50" r="5" fill="url(#ctaGrad)">
    <animate attributeName="r" values="5;8;5" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="730" cy="50" r="5" fill="url(#ctaGrad)">
    <animate attributeName="r" values="5;8;5" dur="2s" begin="0.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="70" cy="150" r="5" fill="url(#ctaGrad)">
    <animate attributeName="r" values="5;8;5" dur="2s" begin="1s" repeatCount="indefinite"/>
  </circle>
  <circle cx="730" cy="150" r="5" fill="url(#ctaGrad)">
    <animate attributeName="r" values="5;8;5" dur="2s" begin="1.5s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Text content -->
  <text x="400" y="75" font-size="28" font-weight="bold" fill="url(#ctaGrad)" text-anchor="middle" filter="url(#ctaGlow)">
    🚀 Let's Build Something Amazing
  </text>
  
  <text x="400" y="110" font-size="18" fill="#ffffff" text-anchor="middle">
    🤖 AI/ML Engineering • 💻 Senior Software Engineering
  </text>
  
  <text x="400" y="140" font-size="18" fill="#ffffff" text-anchor="middle">
    👨‍💼 Technical Leadership • ��️ Developer Tools
  </text>
</svg>

**Ready to collaborate on cutting-edge AI projects or build tools that developers love?**  
**I'm always open to interesting conversations and opportunities!**

[![GitHub](https://img.shields.io/badge/GitHub-brandon--fryslie-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/brandon-fryslie)
[![Profile Views](https://komarev.com/ghpvc/?username=brandon-fryslie&style=for-the-badge&color=00D9FF&labelColor=0d1117)](https://github.com/brandon-fryslie)

---

<!-- Epic Footer Wave -->
<svg width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#00D9FF;#7B68EE;#FF1493;#FFD700;#00D9FF" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="25%" style="stop-color:#7B68EE;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#7B68EE;#FF1493;#FFD700;#00D9FF;#7B68EE" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#FF1493;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#FF1493;#FFD700;#00D9FF;#7B68EE;#FF1493" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="75%" style="stop-color:#FFD700;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#FFD700;#00D9FF;#7B68EE;#FF1493;#FFD700" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0.8">
        <animate attributeName="stop-color" values="#00D9FF;#7B68EE;#FF1493;#FFD700;#00D9FF" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    
    <filter id="footerGlow">
      <feGaussianBlur stdDeviation="5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Multi-layer waves -->
  <path d="M0,60 Q150,30 300,60 T600,60 T900,60 L900,150 L0,150 Z" fill="url(#footerGrad)" opacity="0.3" filter="url(#footerGlow)">
    <animate attributeName="d" 
             values="M0,60 Q150,30 300,60 T600,60 T900,60 L900,150 L0,150 Z;
                     M0,60 Q150,90 300,60 T600,60 T900,60 L900,150 L0,150 Z;
                     M0,60 Q150,30 300,60 T600,60 T900,60 L900,150 L0,150 Z"
             dur="4s" repeatCount="indefinite"/>
  </path>
  
  <path d="M0,80 Q200,50 400,80 T800,80 L800,150 L0,150 Z" fill="url(#footerGrad)" opacity="0.5" filter="url(#footerGlow)">
    <animate attributeName="d" 
             values="M0,80 Q200,50 400,80 T800,80 L800,150 L0,150 Z;
                     M0,80 Q200,110 400,80 T800,80 L800,150 L0,150 Z;
                     M0,80 Q200,50 400,80 T800,80 L800,150 L0,150 Z"
             dur="3s" repeatCount="indefinite"/>
  </path>
  
  <!-- Stars/particles -->
  <circle cx="10%" cy="30" r="2" fill="#FFD700" opacity="0.8">
    <animate attributeName="opacity" values="0.8;0.3;0.8" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="30%" cy="50" r="2" fill="#00D9FF" opacity="0.8">
    <animate attributeName="opacity" values="0.8;0.3;0.8" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="70%" cy="40" r="2" fill="#FF1493" opacity="0.8">
    <animate attributeName="opacity" values="0.8;0.3;0.8" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="90%" cy="60" r="2" fill="#7B68EE" opacity="0.8">
    <animate attributeName="opacity" values="0.8;0.3;0.8" dur="2.2s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Footer text -->
  <text x="50%" y="110" font-size="20" fill="#00D9FF" text-anchor="middle" font-weight="bold" filter="url(#footerGlow)">
    "Don't take anything I say too seriously." 😉
  </text>
</svg>

**70+ repositories • 10+ years experience • ∞ curiosity**

![Hit Counter](https://hit.yhype.me/github/profile?user_id=815181)

</div>
