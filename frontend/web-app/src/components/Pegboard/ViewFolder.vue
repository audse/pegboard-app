<script lang="ts" setup>

import Card from './../Elements/Card.vue'
import AddBoard from './Forms/Add/AddBoard.vue'
import EditFolder from './Forms/Edit/EditFolder.vue'

const props = defineProps({
    folder: Object,
})

</script>
<template>

<card class="bg-gray-800">
    <template #header>
        <h2>{{ folder.name }}</h2>
        <add-board :folder-id="folder.id" />
    </template>

    <card v-for="board in folder.boards" :key="board.id" class="bg-gray-700">
        <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
        {{ board.description }}
    </card>

    <template #footer>
        <edit-folder :folder="folder" />
    </template>

</card>

</template>
<script lang="ts">

export default {
    name: 'ViewFolder',
}

</script>