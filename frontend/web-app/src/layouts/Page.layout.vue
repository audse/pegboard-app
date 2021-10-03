<script lang="ts" setup>

</script>
<template>

<article>

    <header class="header px-4 lg:pl-6 lg:pr-10 pt-8 pb-4 bg-scale-secondary-100 shadow-sm">
        <slot name="header" />
    </header>

    <section class="lg:pl-6 lg:pr-10 pt-8">
        <slot />
    </section>

</article>

</template>
<script lang="ts">

export default {
    name: 'Page'
}

</script>
<style scoped>

.header {
    border-bottom: 1px solid var(--secondary);
}


</style>
