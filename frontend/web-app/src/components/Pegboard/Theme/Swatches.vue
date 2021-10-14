<script lang="ts" setup>

import chroma from 'chroma-js'
import { computed } from 'vue'

const props = defineProps<{
    colors?:number,
}>()

const emits = defineEmits([
    'pick'
])

const numColors = computed( () => props.colors ? props.colors : 10)

const reds = computed( () => chroma.scale(['#550607', '#d90429', '#ffbac6']).colors(numColors.value) )
const oranges = computed( () => chroma.scale(['#731700', '#f54e00', '#ffd1b3']).colors(numColors.value) )
const yellows = computed( () => chroma.scale(['#5e3100', '#ffa91f', '#ffe7bd']).colors(numColors.value) )
const greens = computed( () => chroma.scale(['#0b3023', '#2fa160', '#cef2d9']).colors(numColors.value) )
const blues = computed( () => chroma.scale(['#101d57', '#4361ee', '#d1e0ff']).colors(numColors.value) )
const purples = computed( () => chroma.scale(['#33057d', '#6c26c7', '#e1c4ff']).colors(numColors.value) )
const pinks = computed( () => chroma.scale(['#59004d', '#e349ad', '#ffd1ef']).colors(numColors.value) )
const coolGreys = computed( () => chroma.scale(['#161f29', '#374554', '#c3cbd4']).colors(numColors.value) )

const emitSwatch = (swatch:string) => {
    emits('pick', swatch)
}

</script>
<template>

<article class="swatches">
    <figure v-wave v-for="swatch in reds" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
    <figure v-wave v-for="swatch in oranges" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
    <figure v-wave v-for="swatch in yellows" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
    <figure v-wave v-for="swatch in greens" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
    <figure v-wave v-for="swatch in blues" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
    <figure v-wave v-for="swatch in purples" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
    <figure v-wave v-for="swatch in pinks" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
    <figure v-wave v-for="swatch in coolGreys" :key="swatch" @click="emitSwatch(swatch)" :style="{background:swatch}" />
</article>

</template>
<script lang="ts">
export default {
    name: 'swatches'
}
</script>
<style>

.swatches {
    /* display: flex; */
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-gap: 4pt;
}

.swatches figure {
    @apply rounded-lg block;
    width: 100%;
    padding-bottom: 100%;
    transition: transform 200ms;
}

.swatches figure:hover {
    transform: scale(1.1, 1.1);
}

</style>