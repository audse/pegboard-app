<script lang="ts" setup>

import { ref } from 'vue'

const props = defineProps({
    toShow:Boolean,
})

const show = ref(false)

</script>
<template>
    
<article>

    <section @click="show=!show" class="cursor-pointer flex items-center" v-if="this.$slots.label">

        <transition mode="out-in" name="scale">
            <span v-if="!show || !toShow" class="mr-4">
                <i class="gg-math-plus"></i>
            </span>
            <span v-else class="mr-4">
                <i class="gg-math-minus"></i>
            </span>
        </transition>

        <slot name="label"></slot>
    </section>

    <transition name="slide" class="expanded">
        <section v-show="show || toShow">
            <slot></slot>
        </section>
    </transition>

</article>

</template>
<script lang="ts">

export default {
    name: 'Expandable'
}

</script>
<style scoped>

.expanded {
    transition: max-height 750ms ease;
    height: auto;
    overflow: hidden;
    will-change: max-height;
}

.slide-enter-to, .slide-leave-from {
    max-height: 500pt;
}

.slide-enter-from, .slide-leave-to {
    max-height: 0pt;
}

</style>