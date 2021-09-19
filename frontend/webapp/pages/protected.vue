<template>

    <section class="section">
        {{ $auth }}
        {{ $auth.user.email }}
    </section>

</template>
<script>

export default {
    middleware: 'auth',
}

</script>