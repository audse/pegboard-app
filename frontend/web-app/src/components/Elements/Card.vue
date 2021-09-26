<script lang="ts" setup>

const props = defineProps({

})


</script>
<template>

<article>
    <header>
        <slot name="header"></slot>
    </header>
    <section>
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
}

</style>