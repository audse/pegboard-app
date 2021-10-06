<script lang="ts" setup>

import { reactive } from 'vue'

import { Board } from '@/types'
import { SelectColor } from '@/components'
import { TagService } from '@/services'

const props = defineProps<{
    board:Board
}>()

const addTagForm = reactive({
    name: '',
    color: null,
    board: props.board.id
})

const addTag = async (data:object) => {
    await TagService.create(data)
}

</script>
<template>

<form @submit.prevent="addTag(addTagForm)">
    <section class="flex items-center my-2">
        <label for="name" class="flex-none w-20">Tag Name</label>
        <input v-model="addTagForm.name" name="name" type="text" class="bg-main" />
    </section>
    
    <section class="flex items-center my-2 mb-6">
        <label for="name" class="flex-none w-20">Color</label>
        <select-color v-model="addTagForm.color" :colors="board.colors" />
    </section>
    
    <co-button type="submit" color="emphasis" class="block my-2">Add Tag</co-button>
</form>
    
</template>
<script lang="ts">

export default {
    name: 'add-tag'
}

</script>