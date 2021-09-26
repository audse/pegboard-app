<script lang="ts" setup>

import Card from './../../components/Elements/Card.vue'
import ViewFolder from '../../components/Pegboard/ViewFolder.vue'
import AddFolder from '../../components/Pegboard/Forms/Add/AddFolder.vue'
import AddBoard from '../../components/Pegboard/Forms/Add/AddBoard.vue'

import { onMounted, computed, ref } from 'vue'
import { useStore } from 'vuex'

import FolderService from './../../services/folder.service'
import BoardService from './../../services/board.service'

const store = useStore()

const folders:any = computed( () => store.state.folders.folders )

const refreshFolders = async () => {
    await FolderService.list()
}

const refreshChildren = async () => {
    folders.value.map( (folder:any) => {
        FolderService.listChildren(folder.id).then( (response:{data:object}) => {
            folder.boards = response.data
        }).catch( (e:any) => console.log(e) )
    })
}

const unsortedBoards = computed( () => store.getters['boards/getByFolder']('unsorted') )

const refreshUnsortedBoards = async () => {
    await BoardService.listUnsorted()
}

onMounted( () => {

    refreshUnsortedBoards()
    refreshFolders().then( () => refreshChildren() )

})

</script>
<template>

<article>

    <h1>Folders</h1>

    <section>
        <add-folder />
    </section>

    <section>
        <view-folder v-for="folder in folders" :key="folder.id" :folder="folder" />
    </section>

    <card v-for="board in unsortedBoards" :key="board.id" class="bg-gray-700">
        <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
    </card>

    <section>
        <add-board />
    </section>

</article>

</template>