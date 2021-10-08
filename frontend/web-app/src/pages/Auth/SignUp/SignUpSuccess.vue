<template>

<article>
    <h1>Success</h1>
    <p>You have successfully signed up.</p>

    <router-link :to="{ name: 'Sign In' }">
        <a class="text-blue-500">Sign In</a>
    </router-link>
</article>

</template>