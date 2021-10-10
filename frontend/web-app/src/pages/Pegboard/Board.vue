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
const theme:ComputedRef<Theme> = computed( () => {
    return {
        ...store.state.themes.current,
        // opacity options
    }
})

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

    if(board.value.theme) ThemeService.retrieve(board.value.theme)
})

onBeforeUnmount( () => {
    connection.close()
    store.commit('boards/setCurrent', {})
})

</script>
<template>

<page-layout v-if="board" :class="[board.theme?'theme':'', 'bg-scale-secondary-700']">
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

.theme {
    
    --main: v-bind('theme.main');
    --main-opacity-50: #282c3823;
    --main-opacity-100: #282c383d;
    --main-opacity-300: #282c386e;
    --main-opacity-500: #282c388c;
    --main-opacity-700: #282c38b4;
    --main-opacity-900: #282c38d3;

    --second: v-bind('theme.second');
    --second-opacity-50: #11121323;
    --second-opacity-100: #1112133d;
    --second-opacity-300: #1112136e;
    --second-opacity-500: #1112138c;
    --second-opacity-700: #111213b4;
    --second-opacity-900: #111213d3;

    --text: #f3f7ff;
    --text-opacity-50: #f3f7ff23;
    --text-opacity-100: #f3f7ff3d;
    --text-opacity-300: #f3f7ff6e;
    --text-opacity-500: #f3f7ff8c;
    --text-opacity-700: #f3f7ffb4;
    --text-opacity-900: #f3f7ffd3;

    --emphasis: #f855a6;
    --emphasis-opacity-50: #f855a623;
    --emphasis-opacity-100: #f855a63d;
    --emphasis-opacity-300: #f855a66e;
    --emphasis-opacity-500: #f855a68c;
    --emphasis-opacity-700: #f855a6b4;
    --emphasis-opacity-900: #f855a6d3;

    --alert: #88a4ff;
    --alert-opacity-50: #88a4ff23;
    --alert-opacity-100: #88a4ff3d;
    --alert-opacity-300: #88a4ff6e;
    --alert-opacity-500: #88a4ff8c;
    --alert-opacity-700: #88a4ffb4;
    --alert-opacity-900: #88a4ffd3;

    --danger: #d3a43f;
    --danger-opacity-50: #d3a43f23;
    --danger-opacity-100: #d3a43f3d;
    --danger-opacity-300: #d3a43f6e;
    --danger-opacity-500: #d3a43f8c;
    --danger-opacity-700: #d3a43fb4;
    --danger-opacity-900: #d3a43fd3;

    --scale-text-50: #3E4659;
    --scale-text-50-opacity-50: #3E465923;
    --scale-text-50-opacity-100: #3E46593d;
    --scale-text-50-opacity-300: #3E46596e;
    --scale-text-50-opacity-500: #3E46598c;
    --scale-text-50-opacity-700: #3E4659b4;
    --scale-text-50-opacity-900: #3E4659d3;

    --scale-text-100: #535f79;
    --scale-text-100-opacity-50: #535f7923;
    --scale-text-100-opacity-100: #535f793d;
    --scale-text-100-opacity-300: #535f796e;
    --scale-text-100-opacity-500: #535f798c;
    --scale-text-100-opacity-700: #535f79b4;
    --scale-text-100-opacity-900: #535f79d3;

    --scale-text-300: #6a7692;
    --scale-text-300-opacity-50: #6a769223;
    --scale-text-300-opacity-100: #6a76923d;
    --scale-text-300-opacity-300: #6a76926e;
    --scale-text-300-opacity-500: #6a76928c;
    --scale-text-300-opacity-700: #6a7692b4;
    --scale-text-300-opacity-900: #6a7692d3;

    --scale-text-500: #8692b1;
    --scale-text-500-opacity-50: #8692b123;
    --scale-text-500-opacity-100: #8692b13d;
    --scale-text-500-opacity-300: #8692b16e;
    --scale-text-500-opacity-500: #8692b18c;
    --scale-text-500-opacity-700: #8692b1b4;
    --scale-text-500-opacity-900: #8692b1d3;

    --scale-text-700: #b6bfd4;
    --scale-text-700-opacity-50: #b6bfd423;
    --scale-text-700-opacity-100: #b6bfd43d;
    --scale-text-700-opacity-300: #b6bfd46e;
    --scale-text-700-opacity-500: #b6bfd48c;
    --scale-text-700-opacity-700: #b6bfd4b4;
    --scale-text-700-opacity-900: #b6bfd4d3;

    --scale-text-900: #d1d7e4;
    --scale-text-900-opacity-50: #d1d7e423;
    --scale-text-900-opacity-100: #d1d7e43d;
    --scale-text-900-opacity-300: #d1d7e46e;
    --scale-text-900-opacity-500: #d1d7e48c;
    --scale-text-900-opacity-700: #d1d7e4b4;
    --scale-text-900-opacity-900: #d1d7e4d3;

    --scale-secondary-50: #242831;
    --scale-secondary-50-opacity-50: #24283123;
    --scale-secondary-50-opacity-100: #2428313d;
    --scale-secondary-50-opacity-300: #2428316e;
    --scale-secondary-50-opacity-500: #2428318c;
    --scale-secondary-50-opacity-700: #242831b4;
    --scale-secondary-50-opacity-900: #242831d3;

    --scale-secondary-100: #242831;
    --scale-secondary-100-opacity-50: #24283123;
    --scale-secondary-100-opacity-100: #2428313d;
    --scale-secondary-100-opacity-300: #2428316e;
    --scale-secondary-100-opacity-500: #2428318c;
    --scale-secondary-100-opacity-700: #242831b4;
    --scale-secondary-100-opacity-900: #242831d3;

    --scale-secondary-300: #20232b;
    --scale-secondary-300-opacity-50: #20232b23;
    --scale-secondary-300-opacity-100: #20232b3d;
    --scale-secondary-300-opacity-300: #20232b6e;
    --scale-secondary-300-opacity-500: #20232b8c;
    --scale-secondary-300-opacity-700: #20232bb4;
    --scale-secondary-300-opacity-900: #20232bd3;

    --scale-secondary-500: #1d1f25;
    --scale-secondary-500-opacity-50: #1d1f2523;
    --scale-secondary-500-opacity-100: #1d1f253d;
    --scale-secondary-500-opacity-300: #1d1f256e;
    --scale-secondary-500-opacity-500: #1d1f258c;
    --scale-secondary-500-opacity-700: #1d1f25b4;
    --scale-secondary-500-opacity-900: #1d1f25d3;

    --scale-secondary-700: #191b1f;
    --scale-secondary-700-opacity-50: #191b1f23;
    --scale-secondary-700-opacity-100: #191b1f3d;
    --scale-secondary-700-opacity-300: #191b1f6e;
    --scale-secondary-700-opacity-500: #191b1f8c;
    --scale-secondary-700-opacity-700: #191b1fb4;
    --scale-secondary-700-opacity-900: #191b1fd3;

    --scale-secondary-900: #151719;
    --scale-secondary-900-opacity-50: #15171923;
    --scale-secondary-900-opacity-100: #1517193d;
    --scale-secondary-900-opacity-300: #1517196e;
    --scale-secondary-900-opacity-500: #1517198c;
    --scale-secondary-900-opacity-700: #151719b4;
    --scale-secondary-900-opacity-900: #151719d3;
}

</style>
