<template>

<MainLayout>
<router-view />
</MainLayout>

</template>

<script lang="ts">

import MainLayout from './layouts/Main.layout.vue'

export default {
    components: {
        MainLayout
    }
}

</script>