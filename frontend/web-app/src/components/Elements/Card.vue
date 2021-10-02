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

<div class="wrapper">
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
}

article {
    border-radius: 1rem;

    background-color: v-bind(bgColor);
    border: v-bind(borderStyle);
}

header, footer, .content {
    @apply px-6 py-1;
}

header {
    @apply pt-4;
}

footer {
    @apply pb-4;
}

</style>