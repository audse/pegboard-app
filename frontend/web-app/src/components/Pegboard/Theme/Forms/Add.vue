<script lang="ts" setup>

import { ref, watch, onMounted, computed } from 'vue'
import chroma from 'chroma-js'

import { ExampleTheme } from '@/components'

const name = ref('')
const main = ref('#fefefe')
const second = ref()
const text = ref()
const alert = ref()
const danger = ref()
const scale_secondary = ref([])
const scale_text = ref([])

const autoColor = () => {
    console.log('auto...')
    const luminance = chroma(main.value).luminance()

    second.value = chroma(main.value).darken().hex()
    text.value = luminance>0.5 ? chroma(main.value).darken(3).hex() : chroma(main.value).brighten(3).hex()
    alert.value = luminance>0.5 ? chroma.mix(main.value, '#34c0eb', 0.6, 'lch').darken().hex() : chroma.mix(main.value, '#34c0eb', 0.6, 'lch').brighten().hex()
    danger.value =  luminance>0.5 ? chroma.mix(main.value, '#eba834', 0.6, 'lch').darken().hex() : chroma.mix(main.value, '#eba834', 0.6, 'lch').brighten().hex()

    scale_secondary.value = chroma
        .scale([main.value, second.value])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(5)
    
    scale_text.value = chroma
        .scale([main.value, text.value])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(5)
}

watch(main, () => {
    if ( main.value.length === 7 ) autoColor()
})

onMounted(autoColor)

</script>
<template>

<form>
    <form-text-field v-model="name" name="name" label="Name" required />
    <form-text-field v-model="main" name="main" label="Main Color" required class="mt-6" />
</form>

<example-theme :theme="{ name, main, second, text, scale_secondary, scale_text, alert, danger }" class="mt-10" />

</template>
<script lang="ts">
export default {
    name: 'add-theme'
}
</script>
<style>

</style>