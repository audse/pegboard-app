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
const slotSection = `section=${props.note?.name}`

</script>
<template>

<modal :show="show" :tabs="[note.name, 'Edit', 'Checklists']" @hide="this.$emit('hide')">

    <template v-slot:[slotSection]>
        {{ note.name }}
        {{ note }}
    </template>

    <template #Edit>
        <edit-note :note="note" />
    </template>

</modal>

</template>
<script lang="ts">

export default {
    name: 'NoteModal'
}

</script>