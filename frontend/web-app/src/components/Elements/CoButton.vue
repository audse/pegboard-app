<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps<{

    color?:string,

    outline?:boolean,
    light?:boolean,
    subtle?:boolean,
    round?:boolean,
    icon?:string,
    sm?:boolean,
}>()

const classList = computed( () => {
    let classString = ''
    if (props.round) classString += ' btn btn-circle '
    if (props.outline) classString += 'outline'
    if (props.light) classString += 'light'
    if (props.subtle) classString += 'subtle'
    if (props.color) classString += `-${props.color}`
    if (props.icon) classString += ' flex items-center '
    if (props.sm) classString += ' button-small '
    return classString
})

</script>
<template>

<button v-wave="{initialOpacity:0.3}" :class="[classList,  !this.$slots.default?'button-square':'', 'flex items-center']">
    <icon v-if="icon" :icon="icon" md />
    <span :class="['flex items-center', icon?'ml-2':'']" v-if="this.$slots.default"><slot /></span>
</button>

</template>
<script lang="ts">

export default {
    name: 'co-button',
}

</script>
<style scoped>

.button-small {
    @apply text-sm px-2 py-1;
}

.button-square {
    @apply px-1 py-1;
}

</style>