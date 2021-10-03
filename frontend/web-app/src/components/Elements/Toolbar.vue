<script lang="ts" setup>

const props = defineProps({
    alignTop:Boolean,
    wrap:Boolean,
})

</script>
<template>
    
<nav :class="['toolbar flex', wrap?'flex-wrap':'', !alignTop?'items-center':'items-start']">
    <section class="flex-none flex items-center flex-wrap">
        <slot name="icon" />
    </section>
    <section class="flex-auto flex items-center flex-wrap">
        <slot />
    </section>
    <aside class="toolbar-left flex-1 flex items-center flex-wrap">
        <slot name="left" />
    </aside>
    <aside class="toolbar-right flex-1 flex items-center justify-end flex-wrap">
        <slot name="right" />
    </aside>
</nav>

</template>
<script lang="ts">

export default {
    name: 'Toolbar'
}

</script>