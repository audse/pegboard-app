<script lang="ts" setup>

import SelectColor from './../Select/SelectColor.vue'

import { reactive } from 'vue'

import TagService from './../../../../services/tag.service'

const props = defineProps({
    boardId: Number,
})

const addTagForm = reactive({
    name: '',
    board: props.boardId || undefined
})

const addTag = async (tagId: string, data:object) => {
    await TagService.create(data)
}

</script>
<template>

<form @submit.prevent="addTag(addTagForm, folder.id)">
    <section class="flex items-center">
        <label for="name" class="flex-none">Tag Name</label>
        <input v-model="addTagForm.name" name="name" type="text" placeholder="Tag Name" />
    </section>
    
    <section class="block">
        <label for="name" class="flex-none">Color</label>
        <select-color v-model="addTagForm.color" :boardId="boardId" />
    </section>
    
    <button type="submit" class="flex-none">Add Tag</button>
</form>
    
</template>
<script lang="ts">

export default {
    name: 'AddTag'
}

</script>