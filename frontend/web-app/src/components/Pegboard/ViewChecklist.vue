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
    <li v-for="(item, index) of checklistItems" :key="index" :class="!item.done ? 'opacity-100' : 'opacity-50'">
        <input v-model="item.done" name="done" type="checkbox" class="mr-2" />
        <label for="done">{{ item.name }}</label>
    </li>
</ul>

</template>
<script lang="ts">

export default {
    name: 'ViewChecklist',
}

</script>