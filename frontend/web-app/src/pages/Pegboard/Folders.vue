<template>

<article>

    <h1>Folders</h1>

    <form @submit.prevent="addFolder(addFolderForm)">
        <label for="name">Folder Name</label>
        <input v-model="addFolderForm.name" name="name" type="text" />
        <button type="submit">Add Folder</button>
    </form>

    <section v-for="folder in folders" :key="folder.id">
        <view-folder :folder="folder" />
    </section>

    <section v-for="board in unsortedBoards" :key="board.id" class="p-3 m-3 bg-gray-700">
        <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }">{{ board.name }}</router-link>
    </section>

    <form @submit.prevent="addBoard(addBoardForm)">
        <label for="name">Board Name</label>
        <input v-model="addBoardForm.name" name="name" type="text" />
        <button type="submit">Add Board</button>
    </form>

</article>

</template>

<script components: { ViewFolder } lang="ts" setup>

import { onMounted, watch } from 'vue'
import useFolder from './../../mixins/useFolder'
import useBoard from './../../mixins/useBoard'
import ViewFolder from '../../components/Pegboard/ViewFolder.vue'

const {
    folders,
    refreshFolders,
    refreshChildren,

    addFolderForm,
    addFolder,

} = useFolder()

const {
    unsortedBoards,
    refreshUnsortedBoards,
    refreshParent,

    addBoardForm,
    addBoard
} = useBoard()

onMounted( () => {
    refreshFolders()
    refreshUnsortedBoards()
})

</script>