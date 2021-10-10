<script lang="ts" setup>

import { ref, watch, Ref } from 'vue'

import { ChecklistForm, Board, Page, Note } from '@/types'

const props = defineProps<{
    board?:Board,
    page?:Page,
    note?:Note,
}>()

const checklist:Ref<ChecklistForm> = ref({
    name: 'Checklist',
    items: [],
    board: props.board?.id,
    page: props.page?.id,
    note: props.note?.id,
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
        <label class="w-20">Create</label>
        <co-button @click.prevent="hasChecklist=!hasChecklist" light color="emphasis" class="flex items-center">
            <transition name="scale" mode="out-in">
                <i v-if="!hasChecklist" class="gg-math-plus block flex-none mr-4"></i>
                <i v-else class="gg-math-minus block flex-none mr-4"></i>
            </transition>
            New Checklist
        </co-button>
    </section>

    <expandable :to-show="hasChecklist" class="pt-6 md:pt-4">
        <section class="flex flex-col md:flex-row md:items-center">
            <label for="name" class="flex-none w-20 my-1 md:my-0">Name</label>
            <input v-model="checklist.name" name="name" class="py-3" />
        </section>

        <section v-for="(item, index) of checklist.items" :key="index" class="flex items-center">
            <label class="flex-none md:w-32 text-right text-scale-text-500">{{ index+1 }}</label>
            <input v-model="item.name" />
            <co-button @click.prevent="removeItem(index)" light color="alert" class="ml-2">&times;</co-button>
        </section>

        <section class="md:ml-36 mt-2">
            <co-button @click.prevent="addItem" light color="alert" >Add Item</co-button>
        </section>
    </expandable>

</form>

</template>
<script lang="ts">

export default {
    name: 'add-checklist'
}

</script>