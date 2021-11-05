<script lang="ts" setup>

import { onMounted, Ref, ref, computed } from 'vue'
import FormTextField from './FormTextField.vue'

const props = defineProps<{
    modelValue:string,
}>()

const emits = defineEmits([
    'update:modelValue'
])

const value = computed({
    get: () => props.modelValue,
    set: (value:string) => emits('update:modelValue', value)
})

const textBlock:Ref<any> = ref(null)
const popoverDimensions = ref({
    width: 0,
    height: 0,
})

onMounted(() => {
    console.log(textBlock.value)
    popoverDimensions.value = {
        width: textBlock.value?.clientWidth || 0,
        height: textBlock.value?.clientHeight || 0,
    }
})

</script>
<template>
    
<section ref="textBlock" class="inline-block">
    <slot />
    <section class="popover-box absolute top-0 left-0 flex items-center">
        <form-text-field v-model="value" />
        <co-button subtle color="info">Save</co-button>
    </section>
</section>

</template>
<style scoped>

.popover-box {
    width: v-bind('popoverDimensions.width');
    height: v-bind('popoverDimenstions.height');
    padding: 20px;
}

</style>