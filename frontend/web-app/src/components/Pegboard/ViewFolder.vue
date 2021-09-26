<script lang="ts" setup>
import AddBoard from './Forms/Add/AddBoard.vue'

import EditFolder from './Forms/Edit/EditFolder.vue'

const props = defineProps({
    folder: Object,
})

</script>
<template>

<article class="bg-gray-800 p-3 m-3">
    <h2>{{ folder.name }}</h2>

    <section>
        <add-board :folder-id="folder.id" />
    </section>

    <section v-for="board in folder.boards" :key="board.id" class="bg-gray-700 p-3 m-5">
        <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
    </section>

    <section>
        <edit-folder :folder="folder" />
    </section>

</article>

</template>
<script lang="ts">

export default {
    name: 'ViewFolder',
    components: {
        EditFolder,
        AddBoard,
    }
}

</script>