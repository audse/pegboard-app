<script lang="ts" setup>

import { Ref, ref } from 'vue'

import { Page } from '@/types'
import { ChecklistService } from '@/services'
import { EditPage, Checklist, AddChecklist } from '@/components'

const props = defineProps<{
    page:Page,
    show:boolean,
}>()

const emits = defineEmits([
    'hide'
])

const tabs = ['Edit', 'Checklists']
const tabsSections = (index:number) => `section-${tabs[index]}`

const newChecklist:Ref = ref(null)
const updateChecklist = (event:object) => newChecklist.value = event

const createChecklist = async (data:any) => await ChecklistService.create(data)

</script>
<template>

<modal :tabs="tabs" :show="show" @hide="$emit('hide')">

    <template v-slot:[tabsSections(0)]>        
        <edit-page :page="page" />
    </template>

    <template v-slot:[tabsSections(1)]>
        <h3>Checklists</h3>

        <add-checklist :page="page" @update-checklist="updateChecklist" />
        <co-button v-if="newChecklist" @click.prevent="createChecklist(newChecklist)">Add Checklist</co-button>
        
        <section class="mt-12">
            <checklist v-for="checklist in page.checklists" :key="checklist.id" :checklist="checklist" />
        </section>
    </template>

</modal>

</template>