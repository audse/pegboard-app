<script lang="ts" setup>

import { ref, Ref, watch, onMounted, computed } from 'vue'
import chroma from 'chroma-js'

import { ExampleTheme, Swatches } from '@/components'
import { Themes } from '@/pages'
import { ThemeService } from '@/services'

const name:Ref<string> = ref('')
const main:Ref<string> = ref('#fefefe')
const second:Ref<string> = ref('')
const text:Ref<string> = ref('')
const emphasis:Ref<string> = ref('')
const alert:Ref<string> = ref('')
const danger:Ref<string> = ref('')
const scale_secondary:Ref<Array<string>> = ref([])
const scale_text:Ref<Array<string>> = ref([])

const pickMain = (swatch:string) => {
    console.log(swatch)
    main.value = swatch
}
const autoColor = () => {
    
    const luminance = chroma(main.value).luminance()

    second.value = chroma(main.value).darken().hex()
    text.value = luminance>0.5 ? chroma(main.value).darken(4).hex() : chroma(main.value).brighten(4).hex()
    emphasis.value = luminance>0.5 ? chroma(main.value).set('hsl.h', '*-1').darken().hex() : chroma(main.value).set('hsl.h', '*-1').brighten().hex()
    alert.value = luminance>0.5 ? chroma.mix(main.value, '#34c0eb', 0.6, 'lch').darken().hex() : chroma.mix(main.value, '#34c0eb', 0.6, 'lch').brighten().hex()
    danger.value =  luminance>0.5 ? chroma.mix(main.value, '#eba834', 0.6, 'lch').darken().hex() : chroma.mix(main.value, '#eba834', 0.6, 'lch').brighten().hex()

    scale_secondary.value = chroma
        .scale([main.value, second.value])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(6)
    
    scale_text.value = chroma
        .scale([main.value, text.value])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(6)
}

watch(main, () => {
    if ( main.value.length === 7 ) autoColor()
})

onMounted(autoColor)

const addTheme = async (data:object) => {
    await ThemeService.create(data)
}

</script>
<template>

<form>
    <form-text-field v-model="name" name="name" label="Name" required />
    <form-text-field v-model="main" name="main" label="Main Color" required class="mt-6" />
    <co-button type="submit" @click.prevent="addTheme({ name, main, second, text, scale_secondary, scale_text, emphasis, alert, danger })">
        Add Theme
    </co-button>
</form>

<swatches @pick="pickMain" class="w-1/2 mt-6" />

<example-theme :theme="{ name, main, second, text, scale_secondary, scale_text, emphasis, alert, danger }" class="mt-10" />

</template>
<script lang="ts">
export default {
    name: 'add-theme'
}
</script>
<style>

</style>