<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps({

    color:String,

    outline:Boolean,
    light:Boolean,
    subtle:Boolean,
    round:Boolean,
})

const classList = computed( () => {
    let classString = ''
    if (props.round) classString += ' btn btn-circle '
    if (props.outline) classString += 'outline'
    if (props.light) classString += 'light'
    if (props.subtle) classString += 'subtle'
    if (props.color) classString += `-${props.color}`
    return classString
})

</script>
<template>

<button v-wave="{initialOpacity:0.3}" :class="classList">
    <slot />
</button>

</template>
<script lang="ts">

export default {
    name: 'co-button',
}

</script>