<script lang="ts" setup>

import { reactive, ref, watch } from 'vue'

interface item {
    done:boolean,
    name:string,
}

const hasChecklist = ref(false)
const name = ref('Checklist')
const items:Array<item> = reactive([])
const addItem = () => items.push({ done: false, name: '' })
const removeItem = (index:number) => items.splice(index, 1)

const emits = defineEmits([
    'hasChecklist'
])

watch(hasChecklist, () => {
    emits('hasChecklist', hasChecklist)
})

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
            <input v-model="name" name="name" />
            <button @click.prevent="hasChecklist=false" class="secondary">&times;</button>
        </section>

        <section v-for="(item, index) of items" :key="index" class="flex items-center">
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