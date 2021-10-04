<script lang="ts" setup>

import { reactive, watch } from 'vue'

import ChecklistService from './../../services/checklist.service'

const props = defineProps({
    checklist:Object,
})

const checklistItems = reactive([...props.checklist.items])

watch(checklistItems, () => {
    const newData = {...props.checklist}
    newData.items = checklistItems
    ChecklistService.update(newData.id, newData)
})

</script>
<template>

<ul>
    <li class="font-bold">{{ checklist.name }}</li>
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
    name: 'ViewChecklist',
}

</script>