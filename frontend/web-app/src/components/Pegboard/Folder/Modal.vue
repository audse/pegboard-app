<script lang="ts" setup>

import { Folder } from '@/types'
import { EditFolder } from '@/components'

const props = defineProps<{
    folder:Folder,
    show:boolean,
}>()

const emits = defineEmits([
    'hide'
])

</script>
<template>

<modal :tabs="['Edit']" :show="show" @hide="$emit('hide')">

    <template #section-Edit>        
        <edit-folder :folder="folder" />
    </template>

</modal>

</template>