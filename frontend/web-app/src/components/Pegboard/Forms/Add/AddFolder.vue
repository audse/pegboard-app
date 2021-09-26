<script lang="ts" setup>

import { reactive } from 'vue'

import FolderService from './../../../../services/folder.service'

interface folderForm {
    name:string,
}

let addFolderForm:folderForm = reactive({
    name: '',
})

const addFolder = async (boardId: string, data:folderForm) => {
    await FolderService.create(data)
}

</script>
<template> 

<form @submit.prevent="addFolder(addFolderForm)">
    <label for="name">Folder Name</label>
    <input v-model="addFolderForm.name" name="name" type="text" />
    <button type="submit">Add Folder</button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddFolder'
}

</script>