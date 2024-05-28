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
        const JAVA_EDITOR_OPTIONS = {
            mode: "text/x-java",
            theme: "elegant",
            lineNumbers: true,
            indentUnit: 4,
            autoCloseBrackets: true,
        };

        const PYTHON_EDITOR_OPTIONS = {
            mode: "python",
            theme: "elegant",
            lineNumbers: true,
            readOnly: true,
        };

        let javaEditor = CodeMirror.fromTextArea(
            document.getElementById("java-editor"), JAVA_EDITOR_OPTIONS
        );

        let pythonEditor = CodeMirror.fromTextArea(
            document.getElementById("python-editor"), PYTHON_EDITOR_OPTIONS
        );

        const EDITOR_WIDTH = "30%"
        const EDITOR_HEIGHT = "30vh"

        pythonEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);
        javaEditor.setSize(EDITOR_WIDTH, EDITOR_HEIGHT);
    },
}

</script>
