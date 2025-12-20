# Java → Python Transpiler

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
[![TypeScript](https://img.shields.io/badge/TypeScript-%2352B0D8.svg?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/tailwindcss-3.x-38b2ac?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Vue 3](https://img.shields.io/badge/vue-3.x-42b883?logo=vue.js&logoColor=white)](https://vuejs.org/)


A lightweight frontend pairing a Java editor with live Python transpilation.

## Demo

![Demo placeholder](https://via.placeholder.com/900x320.png?text=Java+→+Python+Transpiler+Demo+Placeholder)

## Quickstart (frontend)
Prerequisites:
- Node.js (20+ recommended)
- npm
- Python (3.11+)

### Install

```bash
npm install
```

### Run development server

```bash
npm run dev
```

### Run e2e tests (headless)

```bash
npx cypress run
```

## Features
- Dual-pane editor: Java input and Python output (CodeMirror integration).
- Debounced/settled-change polling to avoid excessive API calls.
- Responsive layout tuned for ease of use.

## Transpilation
See the transpiler source code [here](https://github.com/8SIXSect/JavaToPythonTranspiler)

## License

MIT License. See [LICENSE](./LICENSE) for details.
