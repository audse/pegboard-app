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
        {{ folder.name }}
        <ul>
            <li v-for="board in folder.boards" :key="board.id">
                <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">
                    {{ board.name }}
                </router-link>
            </li>
        </ul>
    </li>

    <li v-for="board in unsortedBoards" :key="board.id">
        <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">
            {{ board.name }}
        </router-link>
    </li>

</ul>

</template>