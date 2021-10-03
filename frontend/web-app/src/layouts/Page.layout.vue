<script lang="ts" setup>

</script>
<template>

<article>

    <header class="header pl-6 pr-10 pt-8 pb-4 bg-scale-secondary-100 shadow-sm">
        <slot name="header" />
    </header>

    <section>
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
