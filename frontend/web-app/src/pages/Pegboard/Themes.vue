<script lang="ts" setup>

import { computed, ComputedRef } from 'vue'
import { useStore } from 'vuex'

import { Theme as ThemeType } from '@/types'
import { ThemeService } from '@/services'
import { AddTheme } from '@/components'

const store = useStore()

const themes:ComputedRef<Array<ThemeType>> = computed( () => store.state.themes.items )
const refreshThemes = async () => {
    await ThemeService.list()
}

</script>
<template>
    
<page-layout>

    <template #header>
        <h1>Themes</h1>
    </template>
    
    <section class="page-padding">
        <h2>Add Theme</h2>
        <add-theme />

        <!-- <theme v-for="theme of themes" :key="theme.id" :theme="theme" /> -->

    </section>

</page-layout>

</template>
<script lang="ts">
export default {
    name: 'Themes'
}
</script>