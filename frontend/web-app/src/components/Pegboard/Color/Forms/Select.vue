<script lang="ts" setup>

import { onMounted, ref, Ref } from 'vue'
import { useStore } from 'vuex'

import { Color } from '@/types'
import { ColorService } from '@/services'

const props = defineProps<{
    modelValue?:number,
    colors:Array<Color>
}>()

</script>
<template>

<co-tag hover
v-for="color in colors"
:key="color.id"
@click="this.$emit('update:modelValue', color.id)"
:label="color.name"
:color="color.code"
:class="['tag', modelValue===color.id?'selected':'', 'cursor-pointer m-1']"
/>

</template>
<script lang="ts">

export default {
    name: 'select-color',
}

</script>

<style scoped>

.tag {
    @apply cursor-pointer;
    border: 2px solid transparent;
    transition: border 200ms;
}

.selected {
    @apply backdrop-filter backdrop-invert-5;
    border-color: var(--alert);
}

</style>