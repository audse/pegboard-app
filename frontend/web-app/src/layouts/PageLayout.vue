<script lang="ts" setup>

</script>
<template>

<article>
    <header class="page-header px-4 lg:pl-6 lg:pr-10 pt-8 pb-4 bg-scale-secondary-100 shadow-sm">
        <slot name="header" />
    </header>

    <section id="page-root" class="bg-scale-secondary-700 pb-40">
        <slot />
    </section>

    <footer>
        
    </footer>

</article>

</template>
<script lang="ts">

export default {
    name: 'page-layout'
}

</script>
<style>

.page-header {
    border-bottom: 1px solid var(--secondary);
}

.page-padding {
    @apply  px-4 md:px-6 lg:px-6 lg:pr-10 pt-8;
}


</style>
