<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps<{
    bg?:string,
    hexBg?:string,
    border?:string,
    centerContent?:boolean,
    hover?:boolean,
    dense?:boolean,

    topBg?:string,
    topHexBg?:string,
}>()

const bgColor = computed( () => {
    if (props.bg) return `var(--${props.bg})`
    if (props.hexBg) return props.hexBg
    else return 'transparent'
})
const topBgColor = computed( () => {
    if (props.topBg) return `var(--${props.topBg}`
    if (props.topHexBg) return props.topHexBg
    else return 'transparent'
})
const borderStyle = props.border ? `1.5pt solid var(--${props.border})` : 'transparent'

</script>
<template>

<div :class="['wrapper', hover?'wrapper-hover':'']">
<article v-wave="{initialOpacity:hover?0.1:0,finalOpacity:0}" :class="['no-scrollbar', dense?'card-dense':'card']">
    <header v-if="this.$slots.header">
        <slot name="header"></slot>
    </header>
    <section :class="['content', centerContent?'center-content':'']" v-if="this.$slots.default">
        <slot></slot>
    </section>
    <footer v-if="this.$slots.actions">
        <section class="actions">
            <slot name="actions"></slot>
        </section>
    </footer>
    <footer v-if="this.$slots.footer">
        <slot name="footer"></slot>
    </footer>
</article>
</div>

</template>
<script lang="ts">

export default {
    name: 'Card'
}

</script>
<style scoped>

.wrapper {
    @apply p-2;
    transition: transform 200ms;
    max-height: 100%;
}

.wrapper-hover:hover {
    transform: scale(1.02, 1.02);
}

article.card, article.card-dense {
    @apply shadow-md rounded-2xl;

    background-color: v-bind(bgColor);
    border: v-bind(borderStyle);
    max-height: 100%;
    overflow: scroll;
}

article.card-dense {
    @apply rounded-xl;
}

article.card header,
article.card footer,
article.card .content,
article.card .actions {
    @apply px-6 py-1;
}

article.card-dense header,
article.card-dense footer,
article.card-dense .content,
article.card-dense .actions {
    @apply px-6 py-1;
}

.center-content {
    @apply flex items-center justify-center;
}

article.card header {
    @apply pt-4;
    background-color: v-bind(topBgColor);

}

article.card-dense header {
    @apply pt-1;
    background-color: v-bind(topBgColor);
}

article.card footer {
    @apply pb-4;
}

article.card-dense .content {
    @apply bg-emphasis;
}

article.card-dense footer {
    @apply pb-1;
}

</style>