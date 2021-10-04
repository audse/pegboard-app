<template>

<main-layout>
<router-view />
</main-layout>

</template>

<script lang="ts">

import { MainLayout } from '@/layouts'

export default {
    components: {
        MainLayout
    }
}

</script>