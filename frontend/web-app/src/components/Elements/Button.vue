<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps({

    for:String,

    color:String,

    outline:Boolean,
    light:Boolean,
    subtle:Boolean,
    round:Boolean,
    icon:String
})

const classList = computed( () => {
    let classString = ''
    if (props.round) classString += ' btn btn-circle '
    if (props.outline) classString += 'outline'
    if (props.light) classString += 'light'
    if (props.subtle) classString += 'subtle'
    if (props.color) classString += `-${props.color}`
    if (props.icon) classString += ' flex items-center '
    return classString
})

</script>
<template>

<button v-wave="{initialOpacity:0.3}" :class="classList">
    <i :class="`gg-${icon} icon-md flex-none block mr-2`"></i>
    <slot /> 
</button>

</template>
<script lang="ts">

export default {
    name: 'co-button',
}

</script>