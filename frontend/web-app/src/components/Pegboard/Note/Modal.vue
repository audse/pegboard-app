<script lang="ts" setup>

import { EditNote } from '@/components'

const props = defineProps({
    note:Object,
    show:Boolean
})

const emits = defineEmits([
    'hide'
])

const slotLabel = `label-${props.note?.name}`
const slotSection = `section-${props.note?.name}`

</script>
<template>

<modal :show="show" :tabs="[note.name, 'Edit', 'Checklists']" @hide="$emit('hide')">

    <template v-slot:[slotSection]>
        {{ note.name }}
    </template>

    <template #section-Edit>
        <edit-note :note="note" @save="$emit('hide')" />
    </template>

</modal>

</template>
<script lang="ts">

export default {
    name: 'note-modal'
}

</script>