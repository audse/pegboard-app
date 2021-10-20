<script lang="ts" setup>

import { ref, onMounted, watch, toRefs, nextTick } from 'vue'
import parseISO from 'date-fns/parseISO'
import format from 'date-fns/format'

import { Comment } from '@/components'
import { UserComment, Board, Page, Note } from '@/types'

const props = defineProps<{
    comments:Array<UserComment>,
    heightClass?:string,
    board?:Board,
    page?:Page,
    note?:Note,
}>()

const refProps = toRefs(props)

const commentSection:any = ref(null)
const commentContainer:any = ref(null)

onMounted( () => {
    commentContainer.value.scrollTop = commentSection.value.clientHeight
})

watch(refProps.comments, async () => {
    await nextTick()
    commentContainer.value.scrollTop = commentSection.value.clientHeight
})

defineExpose({
    commentContainer
})

const parseDate = (date) => format(parseISO(props.note.date_created), 'MMM d, h:mm aaaa') || ''


</script>
<template>

<section ref="commentContainer" :class="['comment-container', heightClass?heightClass:'max-h-48','overflow-x-scroll']">
    <div ref="commentSection" class="comment-section h-full">

        <span v-if="board" class="block mb-2 text-scale-text-300">
            This board was created by
            <strong>{{ board.user.username }}</strong>
            on {{ parseDate(board.date_created) }}
        </span>

        <span v-if="page" class="block mb-2 text-scale-text-300">
            This page was created by
            <strong>{{ page.user.username }}</strong>
            on {{ parseDate(page.date_created) }}
        </span>
        <span v-if="note" class="block mb-2 text-scale-text-300">
            This note was created by 
            <strong>{{ note.user.username }}</strong>
            on {{ parseDate(note.date_created) }}
        </span>
        
        <comment v-for="comment in comments" :comment="comment" :key="comment.id" />
    </div>
</section>

</template>
<style scoped>

.comment-container {
    isolation: isolate;
}

.comment-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--main-opacity-100);
    /* background: linear-gradient(180deg, var(--main-opacity-700) 0%, var(--main-opacity-50) 100%); */
}

</style>