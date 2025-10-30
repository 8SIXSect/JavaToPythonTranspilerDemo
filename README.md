# Java → Python Transpiler

![Build](https://img.shields.io/github/actions/workflow/status/hunterg/JavaToPythonTranspiler/ci.yml?label=build)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Stars](https://img.shields.io/github/stars/hunterg/JavaToPythonTranspiler?style=social)

A focused transpilation tool that converts Java source code into clean, readable Python. This repository contains the frontend client (Vue 3 + Tailwind + CodeMirror) used to edit Java input and display the transpiled Python output produced by a simple HTTP API.

Why this project matters
- Demonstrates language translation logic and engineering trade-offs between readability and fidelity.
- Shows practical experience with frontend tooling, editor integration, and a clear API contract for automated transformation.
- Great portfolio piece for interviews — highlights engineering judgment, UX for developer tools, and full-stack integration.

Demo
- Live demo: (paste demo URL here)
- GIF / short screencast: (drag & drop or link a GIF here)

Quickstart (frontend)
1. Clone
    git clone https://github.com/hunterg/JavaToPythonTranspiler.git
    cd JavaToPythonTranspiler/client
2. Install
    npm install
3. Configure
    Create a .env.local with:
        VUE_APP_API_URL=http://localhost:8000
4. Run
    npm run dev
5. Build
    npm run build

What to expect
- Edit Java in the left pane; after edits settle the client POSTs the Java source to the transpiler API and replaces the right pane with formatted Python.
- Frontend tech: Vue 3 (script setup), Tailwind CSS, CodeMirror for editor UX.
- Editor contract: POST /transpiler/ with JSON { "java_source_code": "<code>" } → returns { "python_source_code": "<code>" }.

API example (curl)
    curl -X POST "$VUE_APP_API_URL/transpiler/" \
        -H "Content-Type: application/json" \
        -d '{"java_source_code":"public class Main { public static void main(String[] a){ System.out.println(\"hi\"); } }"}'

Result (example)
- Response JSON:
    {
        "python_source_code": "class Main:\n    def main(args):\n        print(\"hi\")\n"
    }

Highlights & implementation notes
- The frontend prioritizes a clean developer experience: responsive dual editors, stable polling to avoid unnecessary transpile requests, and a single cohesive dark UI palette.
- Editor sizing and styling are tuned for readability and recruiter-friendly screenshots.
- The repository separates concerns: editor UI (client) and transpilation logic (server/API). This makes it easy to swap the backend implementation (e.g., a Rust-based transpiler, Python parser, or language-server-backed approach).

How to contribute
- Open an issue for feature requests or bugs.
- Fork, create a feature branch, and open a PR with a short description and screenshots for UI changes.
- Keep changes small and focused; include tests or manual verification instructions where applicable.

License
- MIT — see LICENSE for details.

Contact / Attribution
- Repository: https://github.com/hunterg/JavaToPythonTranspiler
- Owner: hunterg (add your email or link here)


