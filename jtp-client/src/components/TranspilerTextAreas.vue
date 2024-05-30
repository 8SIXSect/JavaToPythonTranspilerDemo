<template>
    <div class="flex justify-around">
        <textarea name="java-editor" id="java-editor" spellcheck="false"
            v-model="javaEditorDefaultText" />

        <textarea name="python-editor" id="python-editor" spellcheck="false"
            v-model="pythonEditorDefaultText" />
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

        const EDITOR_WIDTH = "30%"
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
