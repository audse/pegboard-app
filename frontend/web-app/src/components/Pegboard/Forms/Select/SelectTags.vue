<script lang="ts" setup>

import Tag from './../../../Elements/Tag.vue'

import { computed, onMounted, ref } from 'vue'
import { useStore } from 'vuex'

const props = defineProps({
    modelValue: Array,
})

const emits = defineEmits([
    'update:modelValue'
])

const store = useStore()

const tags = computed( () => store.state.boards.currentBoard?.tags )

const selectedTags = computed({
    get () {
        return props.modelValue
    }, set (value) {
        emits('update:modelValue', value)
    }
})

const updateSelectedTags = (tagId:number, array:Array<number>) => {
    const index = array.indexOf(tagId)
    if ( index === -1 ) {
        array.push(tagId)
    } else {
        array.splice(index, 1)
    }
}

</script>
<template>

<section>
    <tag v-for="tag in tags" :key="tag.id" @click="updateSelectedTags(tag.id, selectedTags)" :label="tag.name" :color="tag.color.color" :class="modelValue.indexOf(tag.id)!==-1?'selected tag':'tag'" />
</section>

</template>
<script lang="ts">

export default {
    name: 'SelectColor',
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