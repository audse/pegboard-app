<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps<{
    modelValue:string,
    label:string,
    required?:boolean,
    name?:string,
    placeholder?:string,
    bg?:string,
}>()

const emits = defineEmits([
    'update:modelValue'
])

const value = computed({
    get: () => {
        return props.modelValue
    },
    set: (value:string) => {
        emits('update:modelValue', value)
    }
})

</script>
<template>

<section class="my-2 flex items-start flex-col md:items-center md:flex-row">
    <label :for="name" class="flex-none block w-24 text-scale-text-900">
        {{ label }}
        <small v-if="required" class="text-danger">Required.</small>
    </label>
    <input v-model="value" :name="name" type="text" :placeholder="placeholder" :class="[bg?`bg-${bg}`:'']" />
</section>

</template>
<script lang="ts">
export default {
    name: 'form-text-field'
}
</script>
<style>

</style>