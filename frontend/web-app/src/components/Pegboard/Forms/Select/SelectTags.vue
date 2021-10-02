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

const tags = computed( () => store.state.boards.current?.tags )

const selectedTags = computed({
    get () {
        return props.modelValue
    }, set (value) {
        emits('update:modelValue', value)
    }
})

const updateSelectedTags = (tag:{id:number}, array:Array<object>) => {
    const index = array.findIndex( (entry:{id:number}) => entry.id === tag.id )
    if ( index === -1 ) {
        array.push(tag)
    } else {
        array.splice(index, 1)
    }
}

const tagInSelected = (tag:{id:number}, array:Array<object>) => {
    return array.findIndex( (entry:{id:number}) => entry.id === tag.id ) !== -1
}

</script>
<template>

<section>
    <tag v-for="tag in tags" :key="tag.id" @click="updateSelectedTags(tag, selectedTags)" :label="tag.name" :color="tag.color.color" :class="tagInSelected(tag, selectedTags)?'selected tag':'tag'" />
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