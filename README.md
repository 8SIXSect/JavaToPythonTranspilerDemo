# Java → Python Transpiler (Frontend)

[![Build](https://img.shields.io/github/actions/workflow/status/hunterg/JavaToPythonTranspiler/ci.yml?label=build)](https://github.com/hunterg/JavaToPythonTranspiler/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/hunterg/JavaToPythonTranspiler?style=social)](https://github.com/hunterg/JavaToPythonTranspiler/stargazers)

A lightweight frontend client that pairs a Java editor with an automatic transpilation preview into Python. The UI is designed to showcase the transpilation result clearly and reliably while integrating with a small HTTP-based transpiler service.

Why this project
- Demonstrates program transformation and pragmatic choices that prioritize readable, idiomatic Python output.
- Highlights full-stack engineering: editor integration, efficient polling/debouncing, and a clean API contract for automated conversion.
- Strong portfolio piece for interviews—shows language understanding, API design, and practical engineering trade-offs.

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

Build for production:
```bash
npm run build
# serve the built files or deploy to your preferred static hosting
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

Project structure (high level)
- client/ — Vue 3 frontend (this folder)
  - src/components — editor + header components
  - src/index.css — styling and editor theme overrides
- server/ — (optional) place for the transpiler service (not included here)

Tests / Verification
- Manual: run dev server and exercise common Java snippets to verify readable Python output.
- Automation: recommended to add end-to-end tests that assert the API contract and sample transpilation outputs.

Contributing
- Raise issues for bugs or feature requests.
- Fork, create a feature branch, and open a PR with a clear description and screenshots for UI changes.
- Keep PRs small and focused; include reproduction steps and expected behavior.

Acknowledgements & further work
- This frontend is intentionally minimal so the transpilation logic and examples remain the focus.
- Future improvements: inline source-mapping, richer syntax hints, and optional round-trip checks.

License
This project is licensed under the MIT License — see the `LICENSE` file for details.

Contact
Repository: https://github.com/hunterg/JavaToPythonTranspiler  
Owner: hunterg
