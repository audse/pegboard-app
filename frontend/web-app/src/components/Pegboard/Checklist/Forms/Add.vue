<script lang="ts" setup>

import { ref, watch, Ref } from 'vue'

import { ChecklistForm } from '@/types'

const props = defineProps<{
    boardId?:number,
    pageId?:number,
    noteId?:number,
}>()

const checklist:Ref<ChecklistForm> = ref({
    name: 'Checklist',
    items: [],
    board: props.boardId,
    page: props.pageId,
    note: props.noteId,
})

const hasChecklist = ref(false)

const addItem = () => checklist.value.items.push({ done: false, name: '' })
const removeItem = (index:number) => checklist.value.items.splice(index, 1)

const emits = defineEmits([
    'updateChecklist'
])

const emitChecklist = () => {
    if ( hasChecklist ) {
        emits('updateChecklist', checklist.value)
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
        <label class="w-20">Checklist</label>
        <co-button @click.prevent="hasChecklist=!hasChecklist" light color="emphasis" class="flex items-center">
            <transition name="scale" mode="out-in">
                <i v-if="!hasChecklist" class="gg-math-plus block flex-none mr-4"></i>
                <i v-else class="gg-math-minus block flex-none mr-4"></i>
            </transition>
            Create
        </co-button>
    </section>

    <expandable :to-show="hasChecklist" class="pt-4">
        <section class="flex items-center">
            <label for="name" class="flex-none w-20">Name</label>
            <input v-model="checklist.name" name="name" class="py-3" />
        </section>

        <section v-for="(item, index) of checklist.items" :key="index" class="flex items-center">
            <label class="flex-none w-32 text-right text-scale-text-500">{{ index+1 }}</label>
            <input v-model="item.name" />
            <co-button @click.prevent="removeItem(index)" light color="alert" class="ml-2">&times;</co-button>
        </section>

        <section class="ml-36 mt-2">
            <co-button @click.prevent="addItem" light color="alert" >Add Item</co-button>
        </section>
    </expandable>

</form>

</template>
<script lang="ts">

export default {
    name: 'AddChecklist'
}

</script>