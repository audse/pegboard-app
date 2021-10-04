<script lang="ts" setup>

import { computed, onMounted, ref } from 'vue'
import { useStore } from 'vuex'

import { Tag, Color } from '@/types'

const props = defineProps({
    modelValue: Array,
})

const emits = defineEmits([
    'update:modelValue'
])

const store = useStore()

const tags = computed( () => store.state.boards.current?.tags )

const selectedTags = computed({
    get () {
        return props.modelValue
    }, set (value) {
        emits('update:modelValue', value)
    }
})

const updateSelectedTags = (tag:Tag, array:Array<Tag>) => {
    const index = array.findIndex( (entry:Tag) => entry.id === tag.id )
    if ( index === -1 ) {
        array.push(tag)
    } else {
        array.splice(index, 1)
    }
}

const isTagInSelected = (tag:Tag, array:Array<Tag>) => {
    return array.findIndex( (entry:Tag) => entry.id === tag.id ) !== -1
}

</script>
<template>

<co-tag 
    v-for="tag in tags"
    :key="tag.id" 
    :label="tag.name" :color="tag.color.color" 
    :class="isTagInSelected(tag, selectedTags)?'selected tag':'tag'"
    @click="updateSelectedTags(tag, selectedTags)" 
/>

</template>
<script lang="ts">

export default {
    name: 'select-tags',
}

</script>

<style scoped>

.tag {
    @apply cursor-pointer;
}

.selected {
    border: 2px solid red;
}

</style>