<script lang="ts" setup>

import { ref, computed } from 'vue'
import { useStore } from 'vuex'

import { Tag } from '@/types'

const props = defineProps<{
    varColor?:string,
    color?:string,
    textColor?:string,
    filled?:boolean,
    tag?:Tag,
    label?:string,
    right?:string,
    dense?:boolean,
    lg?:boolean,
    hover?:boolean,
}>()

const store = useStore()

const changeOpacity = (color:string, opacity:number) => {
    const newOpacity = Math.round(Math.min(Math.max(opacity || 1, 0), 1) * 255);
    return color + newOpacity.toString(16).toUpperCase();
}

const tagColor = computed( () => {
    if ( props.tag ) {
        return store.state.boards.current.colors.find( color => color.id === props.tag.color )
    } else return null
})

const textColor = computed( () => {
    if ( props.textColor ) {
        return props.textColor
    } else if ( props.tag ) {
        return `${tagColor.value?.code}`
    } else if ( props.varColor ) {
        return `var(--${props.varColor})`
    } else if ( props.color ) {
        return `${props.color}`
    } else return 'var(--text)'
})

const bgColor = computed( () => {
    if ( props.tag ) {
        return !props.filled ? `${changeOpacity(tagColor.value?.code, 0.25)}` : tagColor.value?.code
    }if ( props.varColor ) {
        return `var(--${props.varColor}-opacity-100`
    } else if ( props.color ) { 
        return !props.filled ? `${changeOpacity(props.color, 0.25)}` : props.color
    } else return 'transparent'
})

</script>
<template>

<span :class="['tag', dense?'tag-dense':'', lg?'tag-large':'', hover?'tag-hover':'']">
    {{ label }}
    <span v-if="right" class="tag-right">{{ right }}</span>
    <slot />
</span>

</template>
<script lang="ts">

export default {
    name: 'co-tag'
}

</script>
<style scoped>

.tag {
    @apply my-1 font-semibold uppercase rounded-full tracking-widest mr-1;
    background-color: v-bind('bgColor');
    color: v-bind('textColor');
    font-size: 0.75em;
    padding: 2pt 6pt;
}

.tag-right {
    @apply px-1;
    opacity: 0.5;
}

.tag-dense {
    padding: 0 4pt;
}

.tag-large {
    font-size: 0.85em;
    padding: 3pt 8pt;
}

.tag-hover {
    transition: transform 200ms;
}

.tag-hover:hover {
    transform: scale(1.05, 1.05);
}

</style>