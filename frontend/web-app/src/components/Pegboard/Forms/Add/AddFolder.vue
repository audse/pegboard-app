<script lang="ts" setup>

import { reactive } from 'vue'

import FolderService from './../../../../services/folder.service'

const addFolderForm = reactive({
    name: '',
})

const addFolder = async (boardId: string, data:object) => {
    await FolderService.create(data)
    addFolderForm.name = ''
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