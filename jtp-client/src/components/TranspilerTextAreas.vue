<template>

    <textarea name="java-editor" id="java-editor" spellcheck="false"
        v-model="javaEditorDefaultText" />
    <textarea name="python-editor" id="python-editor" spellcheck="false"
        v-model="pythonEditorDefaultText" />

</template>

<script>

export default {
    data() {
        return {
            javaEditorDefaultText:  `public class Main {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello, World!");\n\t}\n}`,
            pythonEditorDefaultText: `class Main:\n\tdef main(args):\n\t\tprint("Hello, World!")`,
        }
    }
}

</script>
