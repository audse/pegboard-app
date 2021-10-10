<script lang="ts" setup>

import chroma from 'chroma-js'

const emits = defineEmits([
    'pick'
])

const reds = chroma.scale(['#550607', '#d90429', '#ffbac6']).colors(10)
const oranges = chroma.scale(['#731700', '#f54e00', '#ffd1b3']).colors(10)
const yellows = chroma.scale(['#5e3100', '#ffa91f', '#ffe7bd']).colors(10)
const greens = chroma.scale(['#0b3023', '#2fa160', '#cef2d9']).colors(10)
const blues = chroma.scale(['#101d57', '#4361ee', '#d1e0ff']).colors(10)
const purples = chroma.scale(['#33057d', '#6c26c7', '#e1c4ff']).colors(10)
const pinks = chroma.scale(['#59004d', '#e349ad', '#ffd1ef']).colors(10)
const coolGreys = chroma.scale(['#161f29', '#374554', '#c3cbd4']).colors(10)

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