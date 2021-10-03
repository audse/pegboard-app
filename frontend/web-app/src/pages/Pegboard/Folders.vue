<script lang="ts" setup>

import Page from './../../layouts/Page.layout.vue'
import Card from './../../components/Elements/Card.vue'
import ViewFolder from '../../components/Pegboard/ViewFolder.vue'
import AddFolder from '../../components/Pegboard/Forms/Add/AddFolder.vue'
import AddBoard from '../../components/Pegboard/Forms/Add/AddBoard.vue'

import { onMounted, computed, ref, onBeforeMount } from 'vue'
import { useStore } from 'vuex'

import FolderService from './../../services/folder.service'
import BoardService from './../../services/board.service'
import AuthService from '../../services/auth.service'

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

<page>
    
    <template #header>
        <h1>Folders</h1>

        <section>
            <add-folder />
        </section>
    </template>

    <section>
        <view-folder v-for="folder in folders" :key="folder.id" :folder="folder" />
    </section>

    <section class="mt-12">
        <h2 class="py-4">Unsorted</h2>
        <card v-for="board in unsortedBoards" :key="board.id">
            <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
        </card>
    </section>

    <section>
        <add-board />
    </section>

</page>

</template>