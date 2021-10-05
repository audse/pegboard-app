<script lang="ts" setup>

import { onMounted, ref, Ref } from 'vue'
import { useStore } from 'vuex'

import { Color } from '@/types'
import { ColorService } from '@/services'

const props = defineProps<{
    modelValue:number,
    colors:Array<Color>
}>()

</script>
<template>

<co-tag
v-for="color in colors"
:key="color.id"
@click="this.$emit('update:modelValue', color.id)"
:label="color.name"
:color="color.color"
:class="modelValue===color.id?'selected':''"
/>

</template>
<script lang="ts">

export default {
    name: 'select-color',
}

</script>

<style scoped>

.selected {
    border: 2px solid red;
}

</style>