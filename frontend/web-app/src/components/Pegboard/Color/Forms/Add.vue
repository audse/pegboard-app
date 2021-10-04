<script lang="ts" setup>

import { reactive } from 'vue'

import { ColorService } from '@/services'

const props = defineProps({
    boardId: Number,
})

const addColorForm = reactive({
    name: '',
    color: '',
    board: props.boardId || undefined
})

const addColor = async (data:object) => {
    await ColorService.create(data)
}

</script>
<template>

<form @submit.prevent="addColor(addColorForm)" class="flex items-center">
    <label for="name" class="flex-none">Color Name</label>
    <input v-model="addColorForm.name" name="name" type="text" placeholder="Color Name" />
    <label for="name" class="flex-none">Color Hex Code</label>
    <input v-model="addColorForm.color" name="name" type="text" placeholder="Color Hex Code" />
    <button type="submit" class="flex-none">Add Color</button>
</form>
    
</template>
<script lang="ts">

export default {
    name: 'AddColor'
}

</script>