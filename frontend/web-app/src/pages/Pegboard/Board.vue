<script lang="ts" setup>

import { computed, ComputedRef, onBeforeUnmount, onMounted, ref, Ref, watch } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'

import { Board, Theme } from '@/types'
import { BoardModal, Page, AddPage, Note, AddNote, } from '@/components'
import { ThemeService } from '@/services'

const store = useStore()
const route = useRoute()
const router = useRouter()

let id = ref(route.params.id)
let url = ref(route.params.url)

const board:ComputedRef<Board> = computed( () => store.state.boards.current )

const showEditModal = ref(false)
const showAddPageForm = ref(false)

let connectionUrl = `ws://localhost:8000/ws/api/boards/${id.value}/${url.value}`
let connection = new WebSocket(connectionUrl)

const openConnection = () => {
    connection.send(JSON.stringify({
        action: 'retrieve'
    }))
}

const getConnectionMssage =  (event:{data:string}) => {
    const data:{action:string,response:object} = JSON.parse(event.data)
    if (data.action === 'retrieve') {
        store.commit('boards/setCurrent', data.response)
    }
}

connection.onopen = () => openConnection()
connection.onmessage = (connectionEvent) => getConnectionMssage(connectionEvent)

watch(route, () => {

    id.value = route.params.id
    url.value = route.params.url
    connectionUrl = `ws://localhost:8000/ws/api/boards/${id.value}/${url.value}`

    connection.close()
    connection = new WebSocket(connectionUrl)
    
    connection.onopen = () => openConnection()
    connection.onmessage = (connectionEvent) => getConnectionMssage(connectionEvent)

})

onBeforeUnmount( () => {
    connection.close()
    store.commit('boards/setCurrent', {})
})

</script>
<template>

<page-layout v-if="board">
    <template #header>

        <toolbar no-col>

            <h1 class="pb-1">
                {{ board.name }}
                <h2 class="font-light text-xl text-scale-text-700">
                    {{ board.description }}
                </h2>
            </h1>

            <template #right>
                <co-button @click="showEditModal=!showEditModal" subtle color="scale-text-500" class="flex-none px-4 py-4 ml-4">
                    <i class="gg-options icon-lg"></i>
                </co-button>
            </template>

        </toolbar>

        <toolbar class="mt-4" no-col>
            <router-link :to="{ name: 'Board', params: { id: id, url: url } }" v-slot="{ isActive }">
                <co-button :light="isActive" :subtle="!isActive" :color="isActive?'emphasis':'scale-text-500'">Kanban</co-button>
            </router-link>

            <template #right>
                <co-button light color="alert" icon="user" class="hidden lg:block"></co-button>
                <co-button @click="showAddPageForm=!showAddPageForm" color="emphasis">
                    <switch-icon :switch="showAddPageForm" class="mr-2" />
                    Add Page
                </co-button>
            </template>
        </toolbar>

        <section>
            <expandable :to-show="showAddPageForm">
                <add-page :board="board" class="mt-6 p-4 rounded-2xl bg-scale-secondary-700" />
            </expandable>
        </section>

    </template>

    <section class="flex overflow-x-scroll h-auto no-scrollbar page-padding">
        <page v-for="page in board.pages" :key="page.id" :page="page" :board="board" class="flex-none w-11/12 md:w-5/12 lg:w-4/12" />
    </section>

    <board-modal :board="board" :show="showEditModal" @hide="showEditModal=false" />

    <article class="mt-8 page-padding">
        <section class="flex flex-col md:flex-row md:items-center pl-2 py-4">
            <h2 class="text-scale-text-500 px-4">Unsorted Notes</h2>
            <add-note :board="board" class="md:w-4/12" />
        </section>
        <section class="flex flex-wrap pl-2" v-if="board?.notes?.length > 0">
            <div v-for="note in board.notes" :key="note.id" class="flex-none w-11/12 md:w-5/12 lg:w-4/12">
                <note :note="note" />
            </div>
        </section>
    </article>

</page-layout>
<page-layout v-else></page-layout>

</template>
<style scoped>

.toolbar button {
    @apply mr-2;
}

.toolbar-right button {
    @apply ml-2 mr-0;
}

</style>
