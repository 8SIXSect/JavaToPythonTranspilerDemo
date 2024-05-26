<template>
    <nav class="flex items-center p-2">
        <div id="main-menu-tool-tip">
            <svg class="w-12 h-12 mx-1 p-3 rounded-full hover:bg-stone-200" focusable="false" viewBox="0 0 24 24">
                <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" fill="#5f6368"></path>
            </svg>
            <span id="tool-tip" class="text-sm text-white text-center font-medium bg-zinc-500 rounded-md py-px px-1 mt-1 w-20 z-10 invisible absolute">
                Main menu
            </span>
        </div>
        <h1 class="text-xl font-header font-medium text-zinc-600">Transpiler</h1>
    </nav>
</template>

<style>

#main-menu-tool-tip:hover #tool-tip {
    visibility: visible;
}

</style>

