<script lang="ts" setup>

import { reactive } from 'vue'

import { SelectColor } from '@/components'
import { TagService } from '@/services'

const props = defineProps({
    boardId: Number,
})

const addTagForm = reactive({
    name: '',
    color: undefined,
    board: props.boardId || undefined
})

const addTag = async (data:object) => {
    await TagService.create(data)
}

</script>
<template>

<form @submit.prevent="addTag(addTagForm)">
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
    name: 'add-tag'
}

</script>