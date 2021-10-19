<script lang="ts" setup>

import { ref } from 'vue'

import { AddBoard, FolderModal } from '@/components'

const props = defineProps({
    folder: Object,
})

const showEditModal = ref(false)

</script>
<template>

<card bg="scale-secondary-300" class="mb-4">
    <template #header>
        <toolbar>
            <div>
                <h2 class="pt-4">{{ folder.name }}</h2>
                <h4 class="text-scale-text-300 pb-2">{{ folder.description }}</h4>
            </div>
            <template #right>
                <co-button @click="showEditModal=!showEditModal" icon="options" subtle color="scale-text-500"></co-button>
            </template>
        </toolbar>
    </template>

    <section class="flex flex-wrap">

        <router-link v-for="board in folder.boards" :key="board.id"  :to="{ name: 'Board', params: { id: board.id, url: board.url } }" class="w-full md:w-1/2 lg:w-1/3 xl:w-1/3">
            <card hover bg="main">
                <template #header>
                        {{ board.name }}
                </template>

                {{ board.description }}
                <template #footer v-if="board.description"></template>
            </card>
        </router-link>

    </section>

    <template #footer>
        <add-board :folder="folder" class="pt-4" />
    </template>

    <folder-modal :folder="folder" :show="showEditModal" @hide="showEditModal=false" />
</card>

</template>
<script lang="ts">

export default {
    name: 'folder',
}

</script>