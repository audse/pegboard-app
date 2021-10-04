<script lang="ts" setup>

import { reactive, watch, computed } from 'vue'

import { Checklist, ChecklistItem } from '@/types'
import { ChecklistService } from '@/services'

const props = defineProps<{
    checklist:Checklist,
}>()

const checklistItems = reactive([...props.checklist.items])

watch(checklistItems, () => {
    const newData = {...props.checklist}
    newData.items = checklistItems
    ChecklistService.update(newData.id, newData)
})

const numComplete = computed( () => {
    let result = 0
    for ( const item of checklistItems ) {
        if ( item.done ) result += 1
    }
    return result
})


</script>
<template>

<ul class="mb-3">
    <li class="font-bold">
        <toolbar>
            {{ checklist.name }}
            <template #right>
                <co-tag var-color="scale-text-500" class="mr-1">{{ numComplete }} / {{ checklist.items.length }}</co-tag>
            </template>
        </toolbar>
    </li>
    <li v-for="(item, index) of checklistItems" :key="index" :class="[!item.done ? 'opacity-100' : 'opacity-40', 'flex items-center py-1 checkbox-control']" @click="item.done=!item.done">
        <div :class="['checkmark flex-none', item.done?'checked':'']">
            <input v-wave v-model="item.done" name="done" type="checkbox" class="appearance-none" />
            <i class="gg-check icon-md"></i>
        </div>
        <label for="done" :class="['ml-2', item.done?'line-through':'']">&nbsp;{{ item.name }}&nbsp;</label>
    </li>
</ul>

</template>
<script lang="ts">

export default {
    name: 'checklist',
}

</script>