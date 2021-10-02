<script lang="ts" setup>

import Card from './../Elements/Card.vue'
import AddBoard from './Forms/Add/AddBoard.vue'
import EditFolder from './Forms/Edit/EditFolder.vue'

const props = defineProps({
    folder: Object,
})

</script>
<template>

<card border no-bg>
    <template #header>
        <h2 class="py-4">{{ folder.name }}</h2>
    </template>

    <card v-for="board in folder.boards" :key="board.id">
        
        <template #header>
            <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">
                {{ board.name }}
            </router-link>
        </template>

        {{ board.description }}
    </card>

    <template #footer>
        <!-- <edit-folder :folder="folder" /> -->
        <add-board :folder-id="folder.id" class="pt-4" />
    </template>

</card>

</template>
<script lang="ts">

export default {
    name: 'ViewFolder',
}

</script>