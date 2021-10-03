<template>
    
<nav class="toolbar flex items-center">
    <section class="flex-1 flex items-center">
        <slot />
    </section>
    <aside class="toolbar-right flex-1 flex items-center justify-end">
        <slot name="right" />
    </aside>
</nav>

</template>
<script lang="ts">

export default {
    name: 'Toolbar'
}

</script>