<script lang="ts" setup>

import { ref } from 'vue'
// import { Theme as ThemeType } from '@/types'
import { Theme } from '@/components'

const form = ref({
    name: '',
    main: '',
    second: '',
    text: '',
    scale_secondary: [],
    scale_text: [],
    alert: '',
    danger: ''
})

</script>
<template>

<form>
    <form-text-field v-model="form.name" name="name" label="Name" required />

    <form-text-field v-model="form.main" name="main" label="Main Color" required class="mt-6" />
    <form-text-field v-model="form.second" name="second" label="Secondary Color" />
    <form-text-field v-model="form.text" name="text" label="Text Color" />
</form>

</template>
<script lang="ts">
export default {
    name: 'add-theme'
}
</script>
<style>

</style>