<template>

<page-layout>
    <template #header>
        <h1>Email Confirmed</h1>
    </template>    

    <p>Thank you for confirming your email. Please <router-link to="/signin">sign in.</router-link></p>
</page-layout>

</template>
<script lang="ts">
export default {
    name: 'ConfirmEmailSuccess'
}
</script>