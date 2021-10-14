<script lang="ts" setup>

import { onMounted, computed, ref, onBeforeMount } from 'vue'
import { useStore } from 'vuex'

import { Folder, AddFolder, AddBoard } from '@/components'
import { FolderService, BoardService, AuthService } from '@/services'

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

const showAddFolderForm = ref(false)

</script>
<template>

<page-layout>
    
    <template #header>
        <toolbar>
            <h1>Folders</h1>

            <template #right>
                <co-button @click="showAddFolderForm=!showAddFolderForm" color="emphasis" class="flex-shrink flex items-center pl-2 my-2 lg:my-0">
                    <switch-icon :switch="showAddFolderForm" />
                    Add Folder
                </co-button>
            </template>
        </toolbar>

        <section>
            <expandable :to-show="showAddFolderForm">
                <add-folder class="mt-6 p-4 rounded-2xl bg-scale-secondary-700" />
            </expandable>
        </section> 
    </template>

    <article class="page-padding">
    <section>
        <folder v-for="folder of folders" :key="folder.id" :folder="folder" />
    </section>

    <h2 class="mt-12 px-2 text-scale-text-500">Unsorted</h2>
    <section class="mt-4 flex">
        <section v-for="board of unsortedBoards" :key="board.id" class="flex-none w-full md:w-1/2 lg:w-1/3 xl:w-1/3">
            <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">
                <card hover bg="main">
                    <template #header>
                        <strong>{{ board.name }}</strong>
                    </template>
                    
                    {{ board.description }}

                    <template #footer v-if="board.description">

                    </template>
                </card>
            </router-link>
        </section>
    </section>

    <section class="mt-4 px-2">
        <add-board />
    </section>
    
    </article>

</page-layout>

</template>