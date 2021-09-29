<script lang="ts" setup>

import Card from './../../components/Elements/Card.vue'
import ViewFolder from '../../components/Pegboard/ViewFolder.vue'
import AddFolder from '../../components/Pegboard/Forms/Add/AddFolder.vue'
import AddBoard from '../../components/Pegboard/Forms/Add/AddBoard.vue'

import { onMounted, computed, ref } from 'vue'
import { useStore } from 'vuex'

import FolderService from './../../services/folder.service'
import BoardService from './../../services/board.service'
import AuthService from '../../services/auth.service'

const store = useStore()

const folders:any = computed( () => store.state.folders.folders )
const refreshFolders = async () => {
    // await FolderService.listWithChildren()
}

const unsortedBoards = computed( () => store.getters['boards/getByFolder']('unsorted') )
const refreshUnsortedBoards = async () => {
    // await BoardService.listUnsorted()
}

onMounted( () => {
    refreshUnsortedBoards()
    refreshFolders()
})

const ws = new WebSocket("ws://localhost:8000/ws/api/folders")
ws.onopen = () => {
    ws.send(JSON.stringify({
        action: 'list',
        request_id: new Date().getTime(),
        data: {
            token: FolderService.config.headers['Authorization']
        }
    }))
    console.log('open')
    console.log(FolderService.config.headers['Authorization'])
}
ws.onmessage = (event:any) => {
    console.log(event.data)
}

</script>
<template>

<article>

    <h1>Folders</h1>

    <section>
        <add-folder />
    </section>

    <section>
        <view-folder v-for="folder in folders" :key="folder.folder.id" :folder="folder" />
    </section>

    <section class="mt-12">
        <h2>Unsorted</h2>
        <card v-for="board in unsortedBoards" :key="board.id" class="bg-gray-700">
            <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
        </card>
    </section>

    <section>
        <add-board />
    </section>

</article>

</template>