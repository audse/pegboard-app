<script lang="ts" setup>

import ViewFolder from '../../components/Pegboard/ViewFolder.vue'
import AddFolder from '../../components/Pegboard/Forms/Add/AddFolder.vue'
import AddBoard from '../../components/Pegboard/Forms/Add/AddBoard.vue'

import { onMounted, computed, ref } from 'vue'
import { useStore } from 'vuex'

import FolderService from './../../services/folder.service'


const store = useStore()

const folders:any = computed( () => store.state.folders.folders )

const refreshFolders = async () => {
    await FolderService.list()
}

const refreshChildren = async () => {
    folders.value.map( (folder:any) => {
        listChildren(folder.id).then( (response:any) => {
            folder.boards = response
        })
    })
}

const listChildren = async (folderId:number) => {
    return new Promise( (resolve) => {
        FolderService.listChildren(folderId).then( (response:{data:object}) => {
            resolve(response.data)
        }).catch( (e:any) => console.log(e) )
    })
}

onMounted( () => {

    refreshFolders().then( () => refreshChildren() )

})

</script>
<template>

<article>

    <h1>Folders</h1>

    <section>
        <!-- <add-folder /> -->
    </section>

    <section v-for="folder in folders" :key="folder.id">
        <view-folder :folder="folder" />
    </section>

    <!-- <section v-for="board in unsortedBoards" :key="board.id" class="p-3 m-3 bg-gray-700">
        <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
    </section> -->

    <section>
        <!-- <add-board /> -->
    </section>

</article>

</template>