# Java → Python Transpiler (Frontend)

[![Build](https://img.shields.io/github/actions/workflow/status/hunterg/JavaToPythonTranspiler/ci.yml?label=build)](https://github.com/hunterg/JavaToPythonTranspiler/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
[![TypeScript](https://img.shields.io/badge/TypeScript-%2352B0D8.svg?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/tailwindcss-3.x-38b2ac?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Vue 3](https://img.shields.io/badge/vue-3.x-42b883?logo=vue.js&logoColor=white)](https://vuejs.org/)


A lightweight frontend pairing a Java editor with live Python transpilation.

Demo
- Live demo: (paste demo URL here)
- GIF / short screencast: (replace with a short animated GIF or link)

![Demo placeholder](https://via.placeholder.com/900x320.png?text=Java+→+Python+Transpiler+Demo+Placeholder)

Quickstart (frontend)
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

How it works (user flow)
- Type or paste Java code into the left editor.
- The client waits for edits to settle and then calls the transpiler API.
- The returned Python source is displayed in the right pane and is read-only by default.

API contract (expected)
- Endpoint: POST {VUE_APP_API_URL}/transpiler/
- Request body (JSON):
```json
{ "java_source_code": "<java source here>" }
```
- Response body (JSON):
```json
{ "python_source_code": "<python source here>" }
```

Example (curl)
```bash
curl -X POST "$VUE_APP_API_URL/transpiler/" \
  -H "Content-Type: application/json" \
  -d '{"java_source_code":"public class Main { public static void main(String[] a){ System.out.println(\"hi\"); } }"}'
```

Result (example)
```json
{
  "python_source_code": "class Main:\n    def main(args):\n        print(\"hi\")\n"
}
```

Features
- Dual-pane editor: Java input and Python output (CodeMirror integration).
- Debounced/settled-change polling to avoid excessive API calls.
- Responsive layout tuned for recruiter-friendly screenshots and demos.
- Simple, clear API contract—easy to swap backend implementations.

Tests / Verification
- Manual: run dev server and exercise common Java snippets to verify readable Python output.
- Automation: recommended to add end-to-end tests that assert the API contract and sample transpilation outputs.



License
This project is licensed under the MIT License — see the `LICENSE` file for details.

