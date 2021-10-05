<script lang="ts" setup>

const props = defineProps<{
    switch:boolean,
    iconTrue?:string,
    iconFalse?:string,
}>()

</script>
<template>

<transition name="scale" mode="out-in">
    <i v-if="switch" :class="[iconTrue?iconTrue:'gg-math-minus', 'block flex-none mr-2']"></i>
    <i v-else :class="[iconFalse?iconFalse:'gg-math-plus', 'gg-math-minus block flex-none mr-2']"></i>
</transition>

</template>
<script lang="ts">

export default {
    name: 'switch-icon'
}

</script>