<script lang="ts" setup>

import parseISO from 'date-fns/parseISO'
import format from 'date-fns/format'

import { UserComment } from '@/types'

const props = defineProps<{
    comment:UserComment,
}>()

const commentDate = format(parseISO(props.comment.date_created), 'MMM d, h:m aaaa') || ''

</script>
<template>
    
<article class="pb-4">
    <section class="flex items-center">
        <co-tag :label="comment.user.username" var-color="scale-text-500" dense />
        <small class="ml-2 text-scale-text-500">{{ commentDate }}</small>
    </section>

    <p>{{ comment.content }}</p>
</article>

</template>
<script lang="ts">

export default {
    name: 'view-comment'
}

</script>