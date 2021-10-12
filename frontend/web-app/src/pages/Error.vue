<script lang="ts" setup>

const props = defineProps<{
    status?:number|string,
    message?:string,
}>()

</script>
<template>
    
<page-layout>

    <template #header>
        <h1>
            <small>{{ status }}</small>
            Something went wrong.
        </h1>
    </template>
    
    <section class="page-padding">
        <p>{{ message }}</p>
    </section>

</page-layout>

</template>