<script lang="ts" setup>

import Expandable from './../../../Elements/Expandable.vue'
import Tag from './../../../Elements/Tag.vue'
import AddColor from './../Add/AddColor.vue'

import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'

import ColorService from '../../../../services/color.service'

const props = defineProps({
    modelValue: Number,
    boardId: Number,
})

const store = useStore()

let colors = ref([])
const refreshColors = async () => {
    ColorService.list().then( (results:Array<object>) => {
        colors.value = results
    })
}

onMounted(() => refreshColors())

</script>
<template>

<section>
    
    <tag v-for="color in colors" :key="color.id" @click="this.$emit('update:modelValue', color.id)" :label="color.name" :color="color.color" :class="modelValue===color.id?'selected':''" />
    <br />

    <expandable class="py-4">
        <template #label>Create New Color</template>
        <add-color :boardId="boardId" />
    </expandable>
</section>

</template>
<script lang="ts">

export default {
    name: 'SelectColor',
}

</script>

<style scoped>

.selected {
    border: 2px solid red;
}

</style>