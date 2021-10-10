<script lang="ts" setup>

import { Ref, ref } from 'vue'
import parseISO from 'date-fns/parseISO'
import format from 'date-fns/format'

import { Board } from '@/types'
import { ChecklistService } from '@/services'
import { EditBoard, AddTag, AddColor, SelectTheme, Checklist, AddChecklist } from '@/components'

const props = defineProps<{
    board:Board,
    show:boolean,
}>()

const emits = defineEmits([
    'hide'
])

const tabs = ['Edit', 'Tags', 'Color Palette', 'Checklists']
const tabsSections = (index:number) => `section-${tabs[index]}`

const newChecklist:Ref = ref(null)
const updateChecklist = (event:object) => newChecklist.value = event

const createChecklist = async (data:any) => {
    ChecklistService.create(data)
}

</script>
<template>

<modal :tabs="tabs" :show="show" @hide="$emit('hide')">

    <template v-slot:[tabsSections(0)]>        
        <edit-board :board="board" />
    </template>

    <template v-slot:[tabsSections(1)]>
        <h3>Tags</h3>
        <section class="pt-4 flex flex-col md:flex-row">
            <co-tag lg v-for="tag in board.tags" :key="tag.id" :label="tag.name" :tag="tag" class="m-1" />
        </section>

        <expandable class="mt-8" label="Add Tag">
            <card bg="scale-secondary-500" class="mt-2">
                <add-tag :board="board" />
            </card>
        </expandable>
    </template>

    <template v-slot:[tabsSections(2)]>
        <h3>Theme</h3>

        <h4>Board Theme</h4>
        <select-theme :board="board" />

        <h4>Color Palette</h4>
        <section class="pt-4 flex flex-col md:flex-row">
            <co-tag lg v-for="color in board.colors" :key="color.id" :label="color.name" :right="`${color.code}`" :color="color.code" class="m-1" />
        </section>

        <expandable class="mt-8" label="Add Color">
            <card bg="scale-secondary-500" class="mt-2">
                <add-color :board="board" />
            </card>
        </expandable>
    </template>

    <template v-slot:[tabsSections(3)]>
        <h3>Checklists</h3>

        <add-checklist :board="board" @update-checklist="updateChecklist" />
        <co-button v-if="newChecklist" @click.prevent="createChecklist(newChecklist)">Add Checklist</co-button>
        
        <section class="mt-12">
            <checklist v-for="checklist in board.checklists" :key="checklist.id" :checklist="checklist" />
        </section>
    </template>

</modal>

</template>