<script lang="ts" setup>

import { ref, computed, watch } from 'vue'

import { Note } from '@/types'
import { NoteService } from '@/services'

const props = defineProps<{
    note:Note,
}>()

const truncatedContent = computed( () => {
    if (props.note.content && props.note.content?.length > 140) {
        return `${props.note?.content.substr(0, 140)}...`
    } else return props.note?.content
})

const noteMarkedDone = ref(props.note.marked_done)

watch(noteMarkedDone, async () => await NoteService.update(props.note.id, {marked_done: noteMarkedDone.value}))

const stop = (event:any) => event.stopPropagation()

</script>
<template>
    
<card bg="main" hover>

    <section class="flex items-center mt-1">
        <form-checkbox-field v-model="noteMarkedDone" class="block my-2" @click="stop" />

        <div :class="['flex-1 ml-1', noteMarkedDone?'line-through text-scale-text-500':'']">
            <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :tag="tag" />
            <strong class="block font-medium mt-1">{{ note.name }}</strong>

            <p v-if="truncatedContent" :class="['my-0 py-0 mb-2', noteMarkedDone?'text-scale-text-300':'text-scale-text-500']">
                {{ truncatedContent }}
            </p>
        </div>
    </section>

</card>

</template>