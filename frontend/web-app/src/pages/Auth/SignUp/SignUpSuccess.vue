<template>

<page-layout>
    <template #header>
        <h1>Success</h1>
        <h2 class="text-scale-text-500 font-light">You have successfully signed up.</h2>
    </template>

    <section class="page-padding">
        <router-link :to="{ name: 'Sign In' }">
            <a class="text-blue-500">Sign In</a>
        </router-link>
    </section>
    
</page-layout>

</template>