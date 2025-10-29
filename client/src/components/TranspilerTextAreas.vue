<script setup>
import { ref, onMounted } from 'vue';
import CodeMirror from 'codemirror';
import "codemirror/lib/codemirror.css";
import "codemirror/theme/elegant.css";
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

onMounted(() => {
    const javaTextarea = document.getElementById("java-editor");
    const pythonTextarea = document.getElementById("python-editor");

    const javaEditor = CodeMirror.fromTextArea(javaTextarea, {
        mode: "text/x-java",
        theme: "elegant",
        lineNumbers: true,
        indentUnit: 4,
        autoCloseBrackets: true,
    });

    const pythonEditor = CodeMirror.fromTextArea(pythonTextarea, {
        mode: "python",
        theme: "elegant",
        lineNumbers: true,
        readOnly: true,
    });

    const EDITOR_WIDTH = "40vw";
    const EDITOR_HEIGHT = "30vh";

    pythonEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);
    javaEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);

    CodeMirror.on(javaEditor, "change", function() {
        pythonEditor.setValue("Loading...");
        let previousJavaSourceCode = javaEditor.getValue();

        // small debounce before starting checks
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
</script>

<template>
    <div class="flex w-screen justify-center gap-x-6 pt-2">
        <div class="flex flex-col">
            <h2 class="text-xl font-header font-medium text-zinc-600 pb-1">Java</h2>
            <textarea name="java-editor" id="java-editor" spellcheck="false"
                      v-model="javaEditorDefaultText" />
        </div>
        <div class="flex flex-col">
            <h2 class="text-xl font-header font-medium text-zinc-600 pb-1">Python</h2>
            <textarea name="python-editor" id="python-editor" spellcheck="false"
                      v-model="pythonEditorDefaultText" />
        </div>
    </div>
</template>

<style>
div.CodeMirror.cm-s-elegant {
	border: 1px solid rgba(0,0,0,.12);
    border-radius: 8px;
}

</style>
