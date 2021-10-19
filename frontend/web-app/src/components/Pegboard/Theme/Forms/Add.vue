<script lang="ts" setup>

import { ref, Ref, watch, onMounted, computed } from 'vue'
import chroma from 'chroma-js'

import { ExampleTheme, Swatches } from '@/components'
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

const pickMain = (swatch:string) => main.value = swatch
const pickSecond = (swatch:string) => second.value = swatch

const showAdvanced = ref(false)

const autoColor = () => {
    
    const luminance = chroma(main.value).luminance()

    second.value = chroma(main.value).darken().hex()
    text.value = luminance>0.5 ? chroma(main.value).darken(4).hex() : chroma(main.value).brighten(4).hex()
    emphasis.value = luminance>0.5 ? chroma(main.value).set('hsl.h', '*-1').darken().hex() : chroma(main.value).set('hsl.h', '*-1').brighten().hex()
    alert.value = luminance>0.5 ? chroma.mix(main.value, '#34c0eb', 0.6, 'lch').darken().hex() : chroma.mix(main.value, '#34c0eb', 0.6, 'lch').brighten().hex()
    danger.value =  luminance>0.5 ? chroma.mix(main.value, '#eba834', 0.6, 'lch').darken().hex() : chroma.mix(main.value, '#eba834', 0.6, 'lch').brighten().hex()

    autoScaleSecondary()
    autoScaleText()
}

const autoScaleSecondary = () => {
    scale_secondary.value = chroma
        .scale([main.value, second.value])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(6)
}

const autoScaleText = () => {
    scale_text.value = chroma
        .scale([main.value, text.value])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(6)
}

watch(main, () => {
    if ( main.value.length === 7 && !showAdvanced.value ) autoColor()
})

watch(second, () => {
    if ( second.value.length === 7 ) autoScaleSecondary()
})

watch(text, () => {
    if ( text.value.length === 7 ) autoScaleText()
})

onMounted(autoColor)

const addTheme = async (data:object) => {
    await ThemeService.create(data)
}

</script>
<template>

<form>
    <form-text-field v-model="name" name="name" label="Name" required />

    <color-expandable v-model="main" name="main" label="Main Color" @pick="pickMain" />
    
    <expandable :to-show="showAdvanced">
        <template #label>
            <form-checkbox-field v-model="showAdvanced" label="Show Advanced Options" name="show-advanced" subtle />
        </template>
        
        <color-expandable v-model="second" name="second" label="Second Color" @pick="pickSecond" />
        <color-expandable v-model="text" name="second" label="Text Color" @pick="pickText" />

        <color-expandable v-model="emphasis" name="emphasis" label="Emphasis Color" />
        <color-expandable v-model="alert" name="alert" label="Alert Color" />
        <color-expandable v-model="danger" name="danger" label="Danger Color" />

    </expandable>


    <co-button type="submit" @click.prevent="addTheme({ name, main, second, text, scale_secondary, scale_text, emphasis, alert, danger })">
        Add Theme
    </co-button>
</form>

<example-theme :theme="{ name, main, second, text, scale_secondary, scale_text, emphasis, alert, danger }" class="mt-10" />

</template>
<script lang="ts">
export default {
    name: 'add-theme'
}
</script>
<style>

</style>