<script lang="ts" setup>

import { reactive } from 'vue'

import { PageService } from '@/services'

const props = defineProps({
    page: Object,
})

const editPageForm = reactive({...props.page})

const editPage = async (pageId: string, data:object) => {
    await PageService.update(pageId, data)
}

const archivePage = async(pageId:number) => {
    await PageService.archive(pageId)
}

</script>
<template>

<h3>
    <tag label="edit" var-color="scale-text-500" class="block w-min" />
    {{ page.name }}
</h3>

<form @submit.prevent="editPage(page.id, editPageForm)">

    <section class="pt-6 flex items-center">
        <label for="name" class="flex-none w-24">Name</label>
        <input v-model="editPageForm.name" name="name" type="text" />
    </section>

    <section class="pt-1 flex items-center">
        <label for="description" class="flex-none w-24">Description</label>
        <textarea v-model="editPageForm.description" name="description" type="text" />
    </section>

    <section class="pt-1">
        <button type="submit" @click="this.$emit('save')" class="secondary">Save Edit</button>
    </section>

    <section class="pt-8">
        <button @click.prevent="archivePage(page.id);this.$emit('save')" class="bg-transparent text-red-500">Archive</button>
    </section>
</form>

</template>

<script lang="ts">

export default {
    name: 'EditPage',
}

</script>