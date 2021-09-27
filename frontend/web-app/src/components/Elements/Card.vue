<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps({
    noBg: Boolean,
    border: Boolean,
})

const bgColor = props.noBg ? 'transparent' : 'var(--scale-secondary-1)'
const borderStyle = props.border ? '2px solid var(--scale-secondary-3)' : 'transparent'

</script>
<template>

<article>
    <header>
        <slot name="header"></slot>
    </header>
    <section class="content">
        <slot></slot>
    </section>
    <footer>
        <slot name="footer"></slot>
    </footer>
</article>

</template>
<script lang="ts">

export default {
    name: 'Card'
}

</script>
<style scoped>

article {
    border-radius: 1rem;
    @apply my-3;

    background-color: v-bind(bgColor);
    border: v-bind(borderStyle);
}

header, footer, .content {
    @apply px-6 py-1;
}

header {
    padding-top: 0.5rem;
}

footer {
    padding-bottom: 0.5rem;
}

</style>