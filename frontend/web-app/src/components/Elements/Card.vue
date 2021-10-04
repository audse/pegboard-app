<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps({
    bg:String,
    border:String,
    centerContent:Boolean,
    hover:Boolean,
})

const bgColor = computed( () => props.bg ? `var(--${props.bg})` : 'transparent' )
const borderStyle = props.border ? `1.5pt solid var(--${props.border})` : 'transparent'

</script>
<template>

<div :class="['wrapper', hover?'wrapper-hover':'']">
<article v-wave="{initialOpacity:hover?0.1:0,finalOpacity:0}">
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
}

.wrapper-hover:hover {
    transform: scale(1.02, 1.02);
}

article {
    @apply shadow-md rounded-2xl;

    background-color: v-bind(bgColor);
    border: v-bind(borderStyle);
}

header, footer, .content, .actions {
    @apply px-6 py-1;
}

.center-content {
    @apply flex items-center justify-center;
}

header {
    @apply pt-4;
}

footer {
    @apply pb-4;
}

</style>