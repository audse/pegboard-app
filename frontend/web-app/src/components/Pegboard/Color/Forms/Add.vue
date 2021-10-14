<script lang="ts" setup>

import { reactive } from 'vue'

import { Board } from '@/types'
import { ColorService } from '@/services'
import { Swatches } from '@/components'

const props = defineProps<{
    board:Board,
}>()

const addColorForm = reactive({
    name: '',
    code: '',
    board: props.board.id || undefined
})

const updateCode = (swatch:string) => addColorForm.code = swatch

const addColor = async (data:object) => {
    await ColorService.create(data)
}

</script>
<template>

<form @submit.prevent="addColor(addColorForm)">
    <section class="flex items-center my-2">
        <label for="name" class="flex-none w-20">Name</label>
        <input v-model="addColorForm.name" name="name" type="text" class="bg-main" />
    </section>
    <section class="flex items-center my-2 mb-6">
        <label for="name" class="flex-none w-20">Hex Code</label>
        <input v-model="addColorForm.code" name="name" type="text" placeholder="#FEFEFE" class="bg-main" />
    </section>
    <section class="w-1/2 mb-4">
        <swatches :colors="1" @pick="updateCode" />
    </section>
    <co-button type="submit" color="emphasis" class="block my-2">Add Color</co-button>
</form>
    
</template>
<script lang="ts">

export default {
    name: 'add-color'
}

</script>