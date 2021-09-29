<script lang="ts" setup>

import { reactive } from 'vue'

import FolderService from './../../../../services/folder.service'

const props = defineProps({
    folder: Object,
})

const editFolderForm = reactive({...props.folder})

const editFolder = async (folderId: string, data:object) => {
    await FolderService.update(folderId, data)
}

</script>
<template>
    
<section class="pt-6">
    <h3>Edit {{ folder.name }}</h3>
    <form @submit.prevent="editFolder(folder.id, editFolderForm)">
        <label for="name">Folder Name</label>
        <input v-model="editFolderForm.name" name="name" type="text" />
        <button type="submit" class="secondary">Save Edit</button>
    </form>
</section>

</template>

<script lang="ts">

export default {
    name: 'EditFolder',
}

</script>