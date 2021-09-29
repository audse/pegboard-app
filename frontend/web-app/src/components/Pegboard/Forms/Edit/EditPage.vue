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
   
<section>

    <h3>Edit {{ page.name }}</h3>

    <form @submit.prevent="editPage(page.id, editPageForm)">

        <section class="pt-4 flex items-center">
            <label for="name" class="flex-none">Page Name</label>
            <input v-model="editPageForm.name" name="name" type="text" />
        </section>

        <section class="pt-4 flex items-center">
            <label for="description" class="flex-none">Page Description</label>
            <textarea v-model="editPageForm.description" name="description" type="text" />
        </section>

        <section class="pt-4">
            <button type="submit" @click="this.$emit('save')" class="secondary">Save Edit</button>
        </section>
    </form>
</section>

</template>

<script lang="ts">

export default {
    name: 'EditPage',
}

</script>