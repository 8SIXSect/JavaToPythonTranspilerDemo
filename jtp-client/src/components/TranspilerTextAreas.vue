<template>
    <div class="flex w-screen justify-center gap-x-6 pt-2">
        <div class="flex flex-col ">
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

<script>

import CodeMirror from 'codemirror';
import "codemirror/lib/codemirror.css";
import "codemirror/theme/elegant.css";
import "codemirror/mode/python/python";
import "codemirror/mode/clike/clike";

export default {
    data() {
        return {
            javaEditorDefaultText:  `public class Main {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello, World!");\n\t}\n}`,
            pythonEditorDefaultText: `class Main:\n\tdef main(args):\n\t\tprint("Hello, World!")`,
        }
    },
    mounted() {
        let javaEditor = CodeMirror.fromTextArea(
            document.getElementById("java-editor"), {
                mode: "text/x-java",
                theme: "elegant",
                lineNumbers: true,
                indentUnit: 4,
                autoCloseBrackets: true,
            }
        );

        let pythonEditor = CodeMirror.fromTextArea(
            document.getElementById("python-editor"), {
                mode: "python",
                theme: "elegant",
                lineNumbers: true,
                readOnly: true,
            }
        );

        const EDITOR_WIDTH = "40vw"
        const EDITOR_HEIGHT = "30vh"

        pythonEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);
        javaEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);

        CodeMirror.on(javaEditor, "change", function() {
            pythonEditor.setValue("Loading...");
            let previousJavaSourceCode = javaEditor.getValue();

            setTimeout(1000);
            const intervalId = setInterval(async function() {
                let javaSourceCode = javaEditor.getValue();

                if (previousJavaSourceCode === javaSourceCode) {
                    const BASE_URL = process.env.VUE_APP_API_URL;
                    const FETCH_URL = `${BASE_URL}/transpiler/${javaSourceCode}/`;

                    let response = await fetch(FETCH_URL);
                    response.json().then(jsonData => {
                        pythonEditor.setValue(jsonData.python_source_code);
                    });

                    clearInterval(intervalId);
                }
            }, 1000);
        });
    },
}

</script>

<style>

div.CodeMirror.cm-s-elegant {
	border: 1px solid rgba(0,0,0,.12);
    border-radius: 8px;

}
</style>

