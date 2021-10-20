<script lang="ts" setup>

import { reactive } from 'vue'

import { Page } from '@/types'
import { PageService } from '@/services'

const props = defineProps<{
    page:Page,
}>()

const emits = defineEmits([
    'save'
])

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
    <co-tag label="edit" var-color="scale-text-500" class="block w-min" />
    {{ page.name }}
</h3>

<form @submit.prevent="editPage(page.id, editPageForm)">

    <!-- <section class="pt-6 pb-2 md:pb-0 flex items-start flex-col md:items-center md:flex-row">
        <label for="name" class="flex-none w-24 pl-4 md:pl-0">Name</label>
        <input v-model="editPageForm.name" name="name" type="text" />
    </section> -->

    <form-text-field v-model="editPageForm.name" name="name" label="Name" />
    <form-textarea-field v-model="editPageForm.description" name="description" label="Description" />

    <!-- <section class="pt-4 pb-2 md:pb-0 md:pt-1 flex items-start flex-col md:items-center md:flex-row">
        <label for="description" class="flex-none w-24 pl-4 md:pl-0">Description</label>
        <textarea v-model="editPageForm.description" name="description" type="text" />
    </section> -->

    <section class="pt-4 pl-1 md:pl-20 md:ml-8">
        <button type="submit" @click="this.$emit('save')" class="secondary">Save Edit</button>
    </section>

    <section class="pt-8">
        <button @click.prevent="archivePage(page.id);this.$emit('save')" class="bg-transparent text-red-500">Archive</button>
    </section>
</form>

</template>

<script lang="ts">

export default {
    name: 'edit-page',
}

</script>