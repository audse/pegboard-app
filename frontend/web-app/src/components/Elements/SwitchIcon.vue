<script lang="ts" setup>

const props = defineProps<{
    switch:boolean,
    iconTrue?:string,
    iconFalse?:string,
}>()

</script>
<template>

<transition name="scale" mode="out-in">
    <i v-if="switch" :class="[iconTrue?`gg-${iconTrue}`:'gg-math-minus', 'block flex-none']"></i>
    <i v-else :class="[iconFalse?`gg-${iconFalse}`:'gg-math-plus', 'block flex-none']"></i>
</transition>

</template>
<script lang="ts">

export default {
    name: 'switch-icon'
}

</script>
