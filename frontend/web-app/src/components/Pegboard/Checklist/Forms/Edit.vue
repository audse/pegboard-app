<script lang="ts" setup>

import { ref, watch, Ref } from 'vue'

import { Checklist, ChecklistForm, Board, Page, Note } from '@/types'

const props = defineProps<{
    checklist:Checklist
}>()

const checklistForm:Ref<ChecklistForm> = ref({...props.checklist})

const addItem = () => checklistForm.value.items.push({ done: false, name: '' })
const removeItem = (index:number) => checklistForm.value.items.splice(index, 1)

</script>
<template>
    
<form>

    <label class="block font-bold mb-4">Edit {{ checklistForm.name }}</label>

    <section class="flex items-center">
        <label for="name" class="flex-none w-20">Name</label>
        <input v-model="checklistForm.name" name="name" class="py-3" />
    </section>

    <section v-for="(item, index) of checklistForm.items" :key="index" class="flex items-center">
        <label class="flex-none w-32 text-right text-scale-text-500">{{ index+1 }}</label>
        <input v-model="item.name" />
        <co-button @click.prevent="removeItem(index)" light color="alert" class="ml-2">&times;</co-button>
    </section>

    <section class="ml-36 mt-2">
        <co-button @click.prevent="addItem" light color="alert" >Add Item</co-button>
    </section>

</form>

</template>
<script lang="ts">

export default {
    name: 'edit-checklist'
}

</script>