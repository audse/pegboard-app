<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps<{
    modelValue:boolean,
    label?:string,
    name?:string,
    subtle?:boolean,
}>()

const emits = defineEmits([
    'update:modelValue',
])

const value = computed({
    get: () => props.modelValue,
    set: (value:boolean) => emits('update:modelValue', value)
})

</script>
<template>

<section :class="['flex items-center cursor-pointer checkbox-control', subtle?'checkbox-control-subtle':'']" @click="value=!value">
    <div :class="['checkmark flex-none', value?'checked':'']">
        <input v-wave v-model="value" :name="name" type="checkbox" class="appearance-none" />
        <i class="gg-check icon-md"></i>
    </div>
    <span class="ml-2">
        {{ label }}
        <slot></slot>
    </span>
</section>

</template>