<script lang="ts" setup>

import { ref } from 'vue'
import icons from '@/assets/icons.svg'

const props = defineProps<{
    icon:string,
    lg?:boolean,
    md?:boolean,
    sm?:boolean,
}>()

const link = ref(`${icons}#gg-${props.icon}`)

</script>
<template>

<svg :class="[lg?'lg':md?'md':sm?'sm':'', `icon-${icon}`]">
    <use :xlink:href="link"/>
</svg>

</template>
<script lang="ts">

export default {
    name: 'icon'
}

</script>
<style scoped>

svg {
    width: 1.25em;
    height: 1.25em;
    margin: 0;
    padding: 0;
}

svg.sm {
    width: 1em;
    height: 1em;
}

svg.md {
    width: 1.25em;
    height: 1.25em;
}

svg.lg {
    width: 1.75em;
    height: 1.75em;
}

/*
    Some icons are sized slightly differently...
*/
.icon-color-bucket {
    transform: translateY(-1pt);
}
.icon-folder.lg {
    padding: 3pt;
} .icon-folder.md {
    padding: 1.5pt;
} .icon-folder {
    padding: 1pt;
}

</style>