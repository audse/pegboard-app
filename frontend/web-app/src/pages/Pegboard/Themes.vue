<script lang="ts" setup>

import { computed, ComputedRef, onMounted } from 'vue'
import { useStore } from 'vuex'

import { Theme as ThemeType } from '@/types'
import { ThemeService } from '@/services'
import { Theme, AddTheme } from '@/components'

const store = useStore()

const themes:ComputedRef<Array<ThemeType>> = computed( () => store.state.themes.items )
const refreshThemes = async () => {
    await ThemeService.list()
}

onMounted(refreshThemes)

</script>
<template>
    
<page-layout>

    <template #header>
        <h1>Themes</h1>
    </template>
    
    <section class="page-padding">
        <h2 class="mb-8">
            Add Theme<br />
            <small class="font-light text-scale-text-500">Note: Themes are not currently functional at this time. They can be created, but not used.</small>
        </h2>
        <add-theme />

        <h2 class="mt-16 mb-6">
            Your Themes
        </h2>
        <theme v-for="theme of themes" :key="theme.id" :theme="theme" />

    </section>

</page-layout>

</template>
<script lang="ts">
export default {
    name: 'Themes'
}
</script>