<script lang="ts" setup>

import { ref, computed, ComputedRef, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

import { Theme as ThemeType, Board } from '@/types'
import { BoardService, ThemeService } from '@/services'

const props = defineProps<{
    board:Board,
}>()

const emits = defineEmits([
    'pick'
])

const store = useStore()
const router = useRouter()

const themes:ComputedRef<Array<ThemeType>> = computed( () => store.state.themes.items )
const refreshThemes = async () => {
    await ThemeService.list()
}

onMounted(refreshThemes)

const setTheme = async (theme:ThemeType|null) => {
    await BoardService.update(props.board.id, { theme: theme?.id||null })
    if (theme) ThemeService.setTheme(theme)
    else ThemeService.resetTheme()
}

</script>
<template>

    <section>
        <co-tag label="Remove" @click="setTheme(null)" hover />
        <co-tag v-for="theme of themes" :key="theme.id" @click="setTheme(theme)" :color="theme.main" :text-color="theme.text" :label="theme.name" filled lg class="m-1" hover :active="theme.id===board.theme" />
    </section>

</template>
<script lang="ts">
export default {
    name: 'select-theme'
}
</script>
<style scoped>

.theme {
    transition: transform 200ms;
}

.theme:hover {
    transform: scale(1.1, 1.1);
}

</style>