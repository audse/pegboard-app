<script lang="ts" setup>

import { ref } from 'vue'

const props = defineProps({
    color: String,
    label: String,
})

const changeOpacity = (color, opacity) => {
    const newOpacity = Math.round(Math.min(Math.max(opacity || 1, 0), 1) * 255);
    return color + newOpacity.toString(16).toUpperCase();
}

const textColor = ref( `#${props.color}`)
const bgColor = ref( `#${changeOpacity(props.color, 0.25)}` )

</script>
<template>
    
<span class="tag">
    {{ label }}
</span>

</template>
<script lang="ts">

export default {
    name: 'Tag'
}

</script>
<style scoped>

.tag {
    @apply px-3 py-1 mx-1 my-3 font-semibold uppercase text-xs rounded-full;
    background-color: v-bind('bgColor');
    color: v-bind('textColor');
    letter-spacing: 1pt;
}

</style>