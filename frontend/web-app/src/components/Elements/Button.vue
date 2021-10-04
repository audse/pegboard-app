<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps({

    for:String,

    color:String,

    outline:Boolean,
    light:Boolean,
    subtle:Boolean,
    round:Boolean,
    icon:String,
    sm:Boolean,
})

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

<button v-wave="{initialOpacity:0.3}" :class="[classList,!this.$slots.default?'p-0 m-0':'']">
    <span :class="['flex-none block', !this.$slots.default?'w-8 h-8 flex items-center justify-center':'mr-2']">
        <i :class="`gg-${icon} icon-md`"></i>
    </span>
    <slot /> 
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

</style>