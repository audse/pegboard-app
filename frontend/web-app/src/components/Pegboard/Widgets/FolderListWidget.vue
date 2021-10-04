<script lang="ts" setup>

import { computed, onBeforeMount } from 'vue'
import { useStore } from 'vuex'

import FolderService from './../../../services/folder.service'
import BoardService from './../../../services/board.service'

const store = useStore()

const folders:any = computed( () => store.state.folders.items )
const refreshFolders = async () => {
    await FolderService.list()
}

const unsortedBoards = computed( () => store.state.boards.items )
const refreshUnsortedBoards = async () => {
    await BoardService.listUnsorted()
}

onBeforeMount( () => {
    refreshUnsortedBoards()
    refreshFolders()
})

</script>
<template>

<ul>

    <li v-for="folder in folders" :key="folder.id">
        <ul>
        <li class="px-8 pt-6 pb-1 font-medium uppercase tracking-widest text-scale-text-700">
            {{ folder.name }}
        </li>
        <li v-for="board in folder.boards" :key="board.id" class="pl-4 pr-4 w-full">
            <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }" v-slot="{ isActive }">
                <co-button icon="layout-grid" :subtle="!isActive" :light="isActive" :color="isActive ? 'emphasis' : 'text'" class="w-full py-2 px-4">
                    {{ board.name }}
                </co-button>
            </router-link>
        </li>
        </ul>
    </li>

    <li class="px-8 pt-6 pb-1 font-medium uppercase tracking-widest text-scale-text-500">
        Unsorted
    </li>
    <li v-for="board in unsortedBoards" :key="board.id" class="pl-4 pr-4 w-full">
        <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }" v-slot="{ isActive }">
            <co-button icon="layout-grid" :subtle="!isActive" :light="isActive" :color="isActive ? 'emphasis' : 'text'" class="w-full py-2 px-4">
                {{ board.name }}
            </co-button>
        </router-link>
    </li>

</ul>

</template>
<script lang="ts">

export default {
    name: 'folder-list-widget',
}

</script>
<style scoped>

.uppercase {
    font-size: 0.8em;
}

.border-emphasis {
    transition: all 250ms;
}

</style>