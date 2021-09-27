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

<form @submit.prevent="addFolder(addFolderForm)" class="flex items-center">
    <label for="name" class="flex-none">Folder Name</label>
    <input v-model="addFolderForm.name" name="name" type="text" placeholder="Folder Name" />
    <button type="submit" class="flex-none">Add Folder</button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddFolder'
}

</script>