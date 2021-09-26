<script lang="ts" setup>

const props = defineProps({

})


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
    border-radius: 3.5rem;
    @apply m-2;
}

header, footer, .content {
    @apply px-3 py-1;
}

header {
    padding-top: calc( 3.5rem / 2 );
}

footer {
    padding-bottom: calc( 3.5rem / 2 );
}

</style>