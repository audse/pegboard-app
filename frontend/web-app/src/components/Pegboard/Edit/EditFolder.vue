<template>
    
<section class="pt-6">
    <h3>Edit {{ folder.name }}</h3>
    <form @submit.prevent="editFolder(folder.id, editFolderForm)">
        <label for="name">Folder Name</label>
        <input v-model="editFolderForm.name" name="name" type="text" />
        <button type="submit">Submit</button>
    </form>
</section>

</template>

<script lang="ts">

import { reactive } from 'vue'

import useFolder from './../../../mixins/useFolder'

export default {

    name: 'EditFolder',

    props: {
        folder: Object,
    },

    setup ( props:{folder:object} ) {

        const {
            editFolder
        } = useFolder()

        const editFolderForm = reactive(Object.assign({}, props.folder))

        return {
            editFolder,
            editFolderForm,
        }

    }
}

</script>