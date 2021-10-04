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
                    <transition name="scale" mode="out-in">
                        <i v-if="!showAddFolderForm" class="gg-math-plus block flex-none mr-2"></i>
                        <i v-else class="gg-math-minus block flex-none mr-2"></i>
                    </transition>
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

    <section>
        <folder v-for="folder of folders" :key="folder.id" :folder="folder" />
    </section>

    <section class="mt-6">
        <h2 class="py-4">Unsorted</h2>
        <card v-for="board of unsortedBoards" :key="board.id">
            <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
        </card>
    </section>

    <section>
        <add-board />
    </section>

</page-layout>

</template>