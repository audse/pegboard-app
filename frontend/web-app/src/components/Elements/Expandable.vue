<script lang="ts" setup>

import { ref } from 'vue'

const props = defineProps<{
    toShow:Boolean,
    label?:string
}>()

const show = ref(false)

</script>
<template>
    
<article>

    <section @click="show=!show" class="cursor-pointer flex items-center" v-if="this.$slots.label || this.label">

        <slot name="label">
            <co-button color="emphasis" light class="flex items-center pr-8"> 
                <transition mode="out-in" name="scale">
                    <switch-icon :switch="show||toShow" />
                </transition>
                {{ label }}
            </co-button>
        </slot>
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