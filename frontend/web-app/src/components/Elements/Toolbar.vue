<script lang="ts" setup>

const props = defineProps<{
    alignTop?:boolean,
    noCol?:boolean
}>()

</script>
<template>
    
<nav :class="['toolbar flex md:flex-row', noCol?'flex-row items-center':'flex-col items-start']">
    <section :class="['flex-none flex md:items-center md:flex-row', noCol?'flex-row items-center':'items-start flex-col']">
        <slot name="icon" />
    </section>
    <section :class="['flex-auto flex flex-wrap md:items-center md:flex-row', noCol?'flex-row items-center':'items-start flex-col']">
        <slot />
    </section>
    <aside :class="['toolbar-left flex-1 flex flex-wrap md:items-center md:flex-row', noCol?'flex-row items-center':'items-start flex-col']">
        <slot name="left" />
    </aside>
    <aside :class="['toolbar-right flex-1 flex flex-wrap text-right md:items-center md:flex-row md:justify-end', noCol?'flex-row items-center justify-end':'flex-col justify-end items-end']">
        <slot name="right" />
    </aside>
</nav>

</template>
<script lang="ts">

export default {
    name: 'Toolbar'
}

</script>