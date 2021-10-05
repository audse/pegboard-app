<script lang="ts" setup>

import { ref } from 'vue'

const props = defineProps<{
    varColor?:string,
    color?:string,
    label?:string,
    dense?:boolean,
}>()

const changeOpacity = (color:string, opacity:number) => {
    const newOpacity = Math.round(Math.min(Math.max(opacity || 1, 0), 1) * 255);
    return color + newOpacity.toString(16).toUpperCase();
}

const textColor = props.varColor ? ref(`var(--${props.varColor})`) : ref( `#${props.color}`)
const bgColor = props.varColor ? ref(`var(--${props.varColor}-opacity-100`) : ref( `#${changeOpacity(props.color, 0.25)}` )

</script>
<template>
    
<span :class="['tag', dense?'dense':'']">
    {{ label }}
    <slot />
</span>

</template>
<script lang="ts">

export default {
    name: 'co-tag'
}

</script>
<style scoped>

.tag {
    @apply my-1 font-semibold uppercase rounded-full tracking-widest;
    background-color: v-bind('bgColor');
    color: v-bind('textColor');
    font-size: 0.7em;
    padding: 2pt 6pt;
}

.dense {
    padding: 0 4pt;
}

</style>