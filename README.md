# Java → Python Transpiler (Frontend)

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
- Node.js (16+ recommended)
- An instance of the transpiler API (see API section)

Clone and run locally:
```bash
git clone https://github.com/hunterg/JavaToPythonTranspiler.git
cd JavaToPythonTranspiler/client
npm install
# set API url, for example:
# echo "VUE_APP_API_URL=http://localhost:8000" > .env.local
npm run dev
```


## Example (curl)
```bash
curl -X POST "$VUE_APP_API_URL/transpiler/" \
  -H "Content-Type: application/json" \
  -d '{"java_source_code":"public class Main { public static void main(String[] a){ System.out.println(\"hi\"); } }"}'
```

## Features
- Dual-pane editor: Java input and Python output (CodeMirror integration).
- Debounced/settled-change polling to avoid excessive API calls.
- Responsive layout tuned for recruiter-friendly screenshots and demos.
- Simple, clear API contract—easy to swap backend implementations.

## License

MIT License. See [LICENSE](./LICENSE) for details.
