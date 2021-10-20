<script lang="ts" setup>

import { computed, ComputedRef, onBeforeMount, onBeforeUnmount, onMounted, ref, Ref, watch } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'

import { Board, Theme } from '@/types'
import { BoardModal, Page, AddPage, Note, AddNote, Checklist, Kanban, Calendar } from '@/components'
import { ThemeService } from '@/services'

const store = useStore()
const route = useRoute()
const router = useRouter()

let id = ref(route.params.id)
let url = ref(route.params.url)

const board:ComputedRef<Board> = computed( () => store.state.boards.current )

const view = ref('kanban')
const showEditModal = ref(false)
const showAddPageForm = ref(false)

let connectionUrl = `ws://localhost:8000/ws/api/boards/${id.value}/${url.value}`
let connection = new WebSocket(connectionUrl)

const openConnection = () => {
    connection.send(JSON.stringify({
        action: 'retrieve'
    }))
}

const getConnectionMessage =  (event:{data:string}) => {
    const data:{action:string,response:any} = JSON.parse(event.data)
    if (data.action === 'retrieve') {
        store.commit('boards/setCurrent', data.response)
        if (data.response.theme) refreshTheme(data.response.theme)
    }
}

connection.onopen = () => openConnection()
connection.onmessage = (connectionEvent) => getConnectionMessage(connectionEvent)

watch(route, () => {
    if (route.path.includes('board')) {
        id.value = route.params.id
        url.value = route.params.url
        connectionUrl = `ws://localhost:8000/ws/api/boards/${id.value}/${url.value}`

        connection.close()
        connection = new WebSocket(connectionUrl)
        
        connection.onopen = () => openConnection()
        connection.onmessage = (connectionEvent) => getConnectionMessage(connectionEvent)

        // if (board.value.theme) refreshTheme()
    }
})

const refreshTheme = async (themeId:number) => {
    const currentTheme = await ThemeService.retrieve(themeId)
    ThemeService.setTheme(currentTheme)
}

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
        <section v-if="board.checklists?.length>0" class="my-6">
            <checklist v-for="checklist in board.checklists" :key="checklist.id" :checklist="checklist" />
        </section>

        <toolbar class="mt-4" no-col>

            <co-button :light="view==='kanban'" :subtle="view!=='kanban'" :color="view==='kanban'?'emphasis':'scale-text-500'" @click="view='kanban'">Kanban</co-button>
            <co-button :light="view==='calendar'" :subtle="view!=='calendar'" :color="view==='calendar'?'emphasis':'scale-text-500'" @click="view='calendar'">Calendar</co-button>

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

    <board-modal :board="board" :show="showEditModal" @hide="showEditModal=false" />

    <kanban v-if="view==='kanban'" :board="board" />
    <calendar v-if="view==='calendar'" :board="board" />

</page-layout>

</template>
<style scoped>

.toolbar button {
    @apply mr-2;
}

.toolbar-right button {
    @apply ml-2 mr-0;
}

</style>
