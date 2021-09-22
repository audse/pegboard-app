<template>

<nav class="px-3 pt-5 pb-2">
    <a href="http://localhost:3000/" class="text-blue-500 pr-3">Home</a>
    <a href="http://localhost:8000/admin" class="text-blue-500">Django Admin</a>
    <a href="http://localhost:8000/api" class="text-blue-500">API Root</a>
</nav>
<main class="p-3">
    <slot></slot>
</main>

</template>
<script lang="ts">

export default {
    name: 'MainLayout',
}

</script>