<script lang="ts" setup>

import { reactive } from 'vue'

import PageService from './../../../../services/page.service'

const props = defineProps({
    page: Object,
})

const editPageForm = reactive({...props.page})

const editPage = async (pageId: string, data:object) => {
    await PageService.update(pageId, data)
}

</script>
<template>
   
<section class="pt-6">
    <h3>Edit {{ page.name }}</h3>
    <form @submit.prevent="editPage(page.id, editPageForm)">
        <label for="name">Page Name</label>
        <input v-model="editPageForm.name" name="name" type="text" />
        <button type="submit" class="secondary">Save Edit</button>
    </form>
</section>

</template>

<script lang="ts">

export default {
    name: 'EditPage',
}

</script>