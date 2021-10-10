<script lang="ts" setup>

import { ref, computed, ComputedRef, onMounted } from 'vue'
import { useStore } from 'vuex'

import { Theme as ThemeType } from '@/types'
import { ThemeService } from '@/services'

const emits = defineEmits([
    'pick'
])

const store = useStore()

const themes:ComputedRef<Array<ThemeType>> = computed( () => store.state.themes.items )
const refreshThemes = async () => {
    await ThemeService.list()
}

onMounted(refreshThemes)

const emitSelected = (theme:ThemeType) => {
    emits('pick', theme)
}

</script>
<template>

    <section>
        <co-tag v-for="theme of themes" :key="theme.id" @click="emitSelected(theme)" :color="theme.main" :text-color="theme.text" :label="theme.name" filled lg class="m-1" />
    </section>

</template>
<script lang="ts">
export default {
    name: 'select-theme'
}
</script>