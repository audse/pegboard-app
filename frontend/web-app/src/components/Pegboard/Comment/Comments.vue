<script lang="ts" setup>

import { Comment } from '@/components'
import { UserComment } from '@/types'
import { ref, onMounted, watch, toRefs, nextTick } from 'vue'

const props = defineProps<{
    comments:Array<UserComment>,
    heightClass?:string,
    boardId?:number,
    pageId?:number,
    noteId?:number,
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

</script>
<template>

<section ref="commentContainer" :class="[heightClass?heightClass:'max-h-48','overflow-x-scroll']">
    <div ref="commentSection" class="h-full">
        <comment v-for="comment in comments" :comment="comment" :key="comment.id" />
    </div>
</section>

</template>
<script lang="ts">

export default {
    name: 'comments'
}

</script>