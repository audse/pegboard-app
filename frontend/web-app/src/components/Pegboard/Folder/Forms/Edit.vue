<script lang="ts" setup>

import { ref } from 'vue'

import { FolderService } from '@/services'

const props = defineProps({
    folder: Object,
})

const editFolderForm = ref({...props.folder})

const editFolder = async (folderId: string, data:object) => {
    await FolderService.update(folderId, data)
}

const archiveFolder = async(folderId:number) => {
    await FolderService.archive(folderId)
}

</script>
<template>
    
<section class="pt-6">
    <h3>Edit {{ folder.name }}</h3>
    <form @submit.prevent="editFolder(folder.id, editFolderForm)">

        <form-text-field label="Name" v-model="editFolderForm.name" required name="name" />
        <form-textarea-field label="Description" v-model="editFolderForm.description" name="description" />

        <co-button type="submit" @click="this.$emit('save')" color="emphasis" light>Save Edit</co-button>
    </form>
    
    <section class="pt-8">
        <button @click.prevent="archiveFolder(folder.id);this.$emit('save')" class="bg-transparent text-red-500">Archive</button>
    </section>
</section>

</template>