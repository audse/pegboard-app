<script lang="ts" setup>

import { Swatches } from '@/components'

const props = defineProps<{
    label:string,
    name:string,
    modelValue:string,
}>()

const emits = defineEmits([
    'update:modelValue'
])

const pick = (event:string) => emits('update:modelValue', event)

const stop = (event:any) => event.stopPropagation()

</script>
<template>
    
<expandable>

    <template #label>
        <form-text-field v-model="modelValue" :name="name" :label="label" @click="stop" />
        <co-button icon="color-picker" @click.prevent="" class="ml-2" />
    </template>

    <div class="flex items-center">
        <section class="flex-1">
            <color-picker :color="modelValue" @pick="pick" />
        </section>
        <swatches @pick="pick" class="flex-1" />
    </div>

</expandable>

</template>