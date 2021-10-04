<script lang="ts" setup>

import { AddBoard, EditFolder } from '@/components'

const props = defineProps({
    folder: Object,
})

</script>
<template>

<card bg="scale-secondary-300" class="mb-4">
    <template #header>
        <h2 class="pt-4">{{ folder.name }}</h2>
        <h4 class="text-scale-text-300 pb-2">{{ folder.description }}</h4>
    </template>

    <section class="flex flex-wrap">

    <card center-content border="emphasis-opacity-50" class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4 h-full">
        <co-button icon="math-plus" subtle color="emphasis" class="my-2 mx-0">Add Board</co-button>
    </card>

    <router-link v-for="board in folder.boards" :key="board.id"  :to="{ name: 'Board', params: { id: board.id, url: board.url } }" class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
        <card hover bg="primary">
            <template #header>
                    {{ board.name }}
            </template>

            {{ board.description }}
            <template #footer v-if="board.description"></template>
        </card>
    </router-link>

    </section>

    <template #footer>
        <!-- <edit-folder :folder="folder" /> -->
        <add-board :folder-id="folder.id" class="pt-4" />
    </template>
</card>

</template>
<script lang="ts">

export default {
    name: 'folder',
}

</script>