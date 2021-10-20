<script lang="ts" setup>

import { ref, watch } from 'vue'

import { Theme } from '@/types'
import { ThemeService } from '@/services'
import { autoColor, autoScaleSecondary, autoScaleText } from './utilities/autoColor'

const props = defineProps<{
    theme:Theme,
}>()

const showAdvanced = ref(true)
const showButtons = ref(true)

const themeForm = ref({
    main: props.theme.main,
    second: props.theme.second,
    text: props.theme.text,
    emphasis: props.theme.emphasis,
    alert: props.theme.alert,
    danger: props.theme.danger,
    scale_secondary: props.theme.scale_secondary,
    scale_text: props.theme.scale_text,
})

watch(themeForm.value, () => {
    showButtons.value = true

    themeForm.value.scale_secondary = autoScaleSecondary(themeForm.value.main, themeForm.value.second)
    themeForm.value.scale_text = autoScaleText(themeForm.value.main, themeForm.value.text)

    if (!showAdvanced) {
        const {
            second,
            text,
            emphasis,
            danger,
            alert,
            scaleSecondary,
            scaleText
        } = autoColor(themeForm.value.main)

        themeForm.value.second = second
        themeForm.value.text = text
        themeForm.value.emphasis = emphasis
        themeForm.value.danger = danger
        themeForm.value.alert = alert
        themeForm.value.scale_secondary = scaleSecondary
        themeForm.value.scale_text = scaleText
    }
})

const editTheme = async (themeId:number, data:object) => {
    await ThemeService.update(themeId, data)
}

</script>
<template>

<card :top-hex-bg="theme.second" :hex-bg="theme.scale_secondary[3]" class="theme">

    <template #header>
        <h3 class="theme pt-4 px-6 pb-4">
            {{ theme.name }}
        </h3>
    </template>

    <form @submit.prevent="" id="theme-form">
        <color-expandable v-model="themeForm.main" name="main" label="Main" />

        <expandable :to-show="showAdvanced">
            <template #label>
                <form-checkbox-field v-model="showAdvanced" label="Show Advanced Options" name="show-advanced" subtle />
            </template>
            
            <color-expandable v-model="themeForm.second" name="second" label="Second Color" />
            <color-expandable v-model="themeForm.text" name="second" label="Text Color" />

            <color-expandable v-model="themeForm.emphasis" name="emphasis" label="Emphasis Color" />
            <color-expandable v-model="themeForm.alert" name="alert" label="Alert Color" />
            <color-expandable v-model="themeForm.danger" name="danger" label="Danger Color" />

        </expandable>
    </form>

    <template #footer>
        <toolbar v-if="showButtons" id="actions-root">
            <co-button subtle color="text">Reset Changes</co-button>

            <template #right>
                <co-button color="emphasis" @click="editTheme(theme.id, themeForm)">Save</co-button>
            </template>
        </toolbar>
    </template>

</card>

</template>
<script lang="ts">
export default {
    name: 'theme'
}
</script>
<style scoped>

.theme {
    color: v-bind('theme.text');
}

#theme-form >>> input {
    background: v-bind('theme.second');
}

#theme-form >>> label {
    color: v-bind('theme.text');
}

#theme-form >>> button {
    color: v-bind('theme.text');
    background: v-bind('theme.emphasis');
}

#actions-root {
    --text: v-bind('theme.text');
    --emphasis: v-bind('theme.emphasis');
}

</style>