<template>
    <nav class="flex items-center p-2 border-b">
        <div>
            <svg class="w-12 h-12 mx-1 p-3 hover:bg-stone-200 rounded-full"
                 focusable="false" viewBox="0 0 24 24" role="button">
                <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" fill="#5f6368"></path>
            </svg>
            <span class="text-sm bg-zinc-500 rounded-md py-px px-1 mt-1 w-20">
                Main menu
            </span>
        </div>
        <h1 class="text-xl font-header font-medium text-zinc-600">Transpiler</h1>
        <div class="flex justify-end flex-1">
            <img src="@/assets/erase-icon.svg" alt="Erase Icon" role="button"
                 class="w-12 h-12 hover:bg-stone-200 rounded-full"/>
        </div>
    </nav>
</template>

<style scoped>
nav {
    border-color: rgb(219, 222, 227);
}

span {
    color: white;
    text-align: center;
    font-weight: 500;
    visibility: hidden;
    position: absolute;
    z-index: 10;
}

svg:hover + span {
    visibility: visible;
}
</style>

