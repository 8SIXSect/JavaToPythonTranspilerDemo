<script setup>
import {ref, onMounted} from 'vue';
import CodeMirror from 'codemirror';
import "codemirror/lib/codemirror.css";
import "codemirror/theme/material.css";
import "codemirror/mode/python/python";
import "codemirror/mode/clike/clike";

const javaEditorDefaultText = ref(
    `public class Main {
\tpublic static void main(String[] args) {
\t\tSystem.out.println("Hello, World!");
\t}
}`
);

const pythonEditorDefaultText = ref(
    `class Main:
\tdef main(args):
\t\tprint("Hello, World!")`
);

onMounted(() => {
    const javaTextarea = document.getElementById("java-editor");
    const pythonTextarea = document.getElementById("python-editor");

    const javaEditor = CodeMirror.fromTextArea(javaTextarea, {
        mode: "text/x-java",
        theme: "material",
        lineNumbers: true,
        indentUnit: 4,
        autoCloseBrackets: true,
    });

    const pythonEditor = CodeMirror.fromTextArea(pythonTextarea, {
        mode: "python",
        theme: "material",
        lineNumbers: true,
        readOnly: true,
    });

    // Use parent's full width so editors cannot overflow; height is responsive.
    const EDITOR_WIDTH = "100%";
    const EDITOR_HEIGHT = "48vh";

    pythonEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);
    javaEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);

    CodeMirror.on(javaEditor, "change", function () {
        pythonEditor.setValue("Transpiling...");
        let previousJavaSourceCode = javaEditor.getValue();

        setTimeout(() => {
            let intervalId;
            intervalId = setInterval(() => {
                handlePeriodicTranspile(
                    javaEditor,
                    pythonEditor,
                    previousJavaSourceCode,
                    () => clearInterval(intervalId)
                );
            }, 1000);
        }, 1000);
    });
});

/**
 * Repeatedly checks the Java editor until the text stops changing, then asks the backend
 * to transpile the stable Java code and writes the returned Python code into the Python editor.
 * Once the transpilation completes the provided stopPolling callback is called to stop further checks.
 */
async function handlePeriodicTranspile(javaEditor, pythonEditor, previousJavaSourceCode, stopPolling) {
    let javaSourceCode = javaEditor.getValue();

    if (previousJavaSourceCode === javaSourceCode) {
        const BASE_URL = process.env.VUE_APP_API_URL;
        const FETCH_URL = `${BASE_URL}/transpiler/`;

        try {
            let response = await fetch(FETCH_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    java_source_code: javaSourceCode
                })
            });

            const jsonData = await response.json();
            pythonEditor.setValue(jsonData.python_source_code);
        } catch (e) {
            pythonEditor.setValue("Error fetching transpilation result.");
        }

        stopPolling();
    }
}

</script>

<template>
    <div class="grid gap-6">
        <div class="grid md:grid-cols-2 gap-6 items-start">
            <div class="bg-card-60 border border-muted-weak rounded-xl p-4 shadow-lg-soft">
                <h2 class="text-xl md:text-2xl font-header font-thin text-gray-100 pb-2">Java</h2>
                <textarea name="java-editor" id="java-editor" spellcheck="false"
                          v-model="javaEditorDefaultText"
                          class="w-full h-64 rounded-md bg-transparent text-gray-100"></textarea>
            </div>

            <div class="bg-card-60 border border-muted-weak rounded-xl p-4 shadow-lg-soft">
                <h2 class="text-xl md:text-2xl font-header font-thin text-gray-100 pb-2">Python</h2>
                <textarea name="python-editor" id="python-editor" spellcheck="false"
                          v-model="pythonEditorDefaultText"
                          class="w-full h-64 rounded-md bg-transparent text-gray-100"></textarea>
            </div>
        </div>
        <div class="text-sm text-gray-400">
            Tip: Edit the Java pane; the tool will detect when edits settle and request a transpilation.
        </div>
    </div>
</template>

<style>
/* Further Code Mirror stylign is done in index.css. */
div.CodeMirror {
    max-width: 100%;
}

/* Make the textareas visually consistent while hidden (CodeMirror replaces them) */
textarea {
    font-family: inherit;
    color: #e6eef8;
    background: transparent;
    resize: none;
    max-width: 100%;
    width: 100%;
}
</style>