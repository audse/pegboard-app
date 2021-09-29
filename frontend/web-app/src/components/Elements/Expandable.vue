<script lang="ts" setup>

import { ref } from 'vue'

const show = ref(false)

</script>
<template>
    
<article>
<section @click="show=!show" class="cursor-pointer">
    <span v-if="!show" class="mr-4">&#9660;</span>
    <span v-if="show" class="mr-4">&#9650;</span>
    <slot name="label"></slot>
</section>

<transition name="slide">
    <section v-show="show" class="p-2 ml-1 border-gray-700 border-l">
        <slot></slot>
    </section>
</transition>
</article>

</template>
<style scoped>


</style>