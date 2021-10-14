<script lang="ts" setup>

import { reactive } from 'vue'

import { FolderService } from '@/services'

const addFolderForm = reactive({
    name: '',
})

const addFolder = async (data:object) => {
    await FolderService.create(data)
    addFolderForm.name = ''
}

</script>
<template> 

<form @submit.prevent="addFolder(addFolderForm)">

    <section class="flex items-center">
        <label for="name" class="flex-none block w-24">Name</label>
        <input v-model="addFolderForm.name" name="name" type="text" placeholder="Name" class="bg-main" />
    </section>

    <section class="flex items-center">
        <label for="description" class="flex-none block w-24">Description</label>
        <textarea v-model="addFolderForm.description" name="description" type="text" placeholder="Description" class="bg-main" />
    </section>

    <co-button type="submit" light color="emphasis" icon="math-plus"> Add Folder</co-button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddFolder'
}

</script>