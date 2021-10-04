<script lang="ts" setup>

import parseISO from 'date-fns/parseISO'
import format from 'date-fns/format'

const props = defineProps({
    comment:Object,
})

const commentDate = format(parseISO(props.comment?.date_created), 'MMM d, h:m aaaa') || ''

</script>
<template>
    
<article v-if="comment" class="py-3">
    <label class="font-semibold opacity-75">{{ comment.user.username }}</label>
    <p>{{ comment.content }}</p>
    <small class="opacity-50">{{ commentDate }}</small>
</article>

</template>
<script lang="ts">

export default {
    name: 'ViewComment'
}

</script>