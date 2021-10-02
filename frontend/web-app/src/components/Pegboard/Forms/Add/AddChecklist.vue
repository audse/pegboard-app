<script lang="ts" setup>

import { reactive, ref, watch } from 'vue'

const props = defineProps({
    boardId:Number,
    pageId:Number,
    noteId:Number,
})

interface item {
    done:boolean,
    name:string,
}

interface checklist {
    name:string,
    items:Array<item>,

    board:number|undefined,
    page:number|undefined,
    note:number|undefined,
}

const checklist:checklist = reactive({
    name: 'Checklist',
    items: [],
    board: props.boardId || null,
    page: props.pageId || null,
    note: props.noteId || null,
})

const hasChecklist = ref(false)

const addItem = () => checklist.items.push({ done: false, name: '' })
const removeItem = (index:number) => checklist.items.splice(index, 1)

const emits = defineEmits([
    'updateChecklist'
])

const emitChecklist = () => {
    if ( hasChecklist ) {
        emits('updateChecklist', checklist)
    } else {
        emits('updateChecklist', null)
    }
}

watch(hasChecklist, emitChecklist)
watch(checklist, emitChecklist)

</script>
<template>
    
<form>

    <section class="flex items-center">
        <label>Add Checklist</label>
        <button @click.prevent="hasChecklist=true" v-if="!hasChecklist">Create</button>
    </section>

    <section v-if="hasChecklist">
        <section class="flex items-center">
            <label for="name">Name</label>
            <input v-model="checklist.name" name="name" />
            <button @click.prevent="hasChecklist=false" class="secondary">&times;</button>
        </section>

        <section v-for="(item, index) of checklist.items" :key="index" class="flex items-center">
            <label>{{ index+1 }}</label>
            <input v-model="item.name" />
            <button @click.prevent="removeItem(index)" class="secondary">&times;</button>
        </section>

        <button @click.prevent="addItem" class="secondary">Add Item</button>
    </section>

</form>

</template>
<script lang="ts">

export default {
    name: 'AddChecklist'
}

</script>