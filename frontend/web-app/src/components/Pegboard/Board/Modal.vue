<script lang="ts" setup>

import { Board } from '@/types'
import { AddTag } from '@/components'

const props = defineProps<{
    board:Board,
    show:boolean,
}>()

const emits = defineEmits([
    'hide'
])

const tabs = ['Edit', 'Tags', 'Color Palette']
const tabsLabels = (index:number) => `label-${tabs[index]}`
const tabsSections = (index:number) => `section-${tabs[index]}`

</script>
<template>

<modal :tabs="tabs" :show="show" @hide="$emit('hide')">

    <template v-slot:[tabsSections(0)]>

    </template>

    <template v-slot:[tabsSections(1)]>
        <h3>Tags</h3>
        <section class="pt-4">
            <co-tag v-for="tag in board.tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />
        </section>

        <expandable class="pt-8" label="Add Tag">
            <add-tag :board="board" />
        </expandable>
    </template>

</modal>

</template>