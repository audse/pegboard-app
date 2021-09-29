<script lang="ts" setup>

import AddColor from './../Add/AddColor.vue'

import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'

import ColorService from '../../../../services/color.service'

const props = defineProps({
    modelValue: String,
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
    <span v-for="color in colors" :key="color.id" @click="this.$emit('update:modelValue', color.color)">
        {{ color.name }}
    </span>
    <br />
    <label for="color">Selected: {{ modelValue }}</label>
    <add-color :boardId="boardId" />
</section>

</template>
<script lang="ts">

export default {
    name: 'SelectColor',
}

</script>