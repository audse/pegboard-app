<script lang="ts" setup>

import ColorPickerPlugin from './ColorPickerPlugin.vue'

const props = defineProps<{
    color:string,
}>()

const emits = defineEmits([
    'pick'
])

const changeColor = (newColor:any) => emits('pick', newColor.colors.hex.substr(0, 7))

</script>
<template>

<color-picker-plugin :color="color" @color-change="changeColor" :visible-formats="['hex']" default-format="hex" />

</template>
<style>

.vacp-color-picker {
    --vacp-focus-color: var(--alert);
    --vacp-tiled-background-image: linear-gradient(
      45deg,
      var(--second) 25%,
      transparent 25%,
      transparent 75%,
      var(--second) 75%,
      var(--second)
    ),
    linear-gradient(
      45deg,
      var(--second) 25%,
      transparent 25%,
      transparent 75%,
      var(--second) 75%,
      var(--second)
    );
    background: var(--second);
    color: var(--text);
}

.vacp-color-input {
    @apply rounded-xl;
    background: var(--scale-secondary-500);
    color: var(--text);
    border: transparent;
}

</style>