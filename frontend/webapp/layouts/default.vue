<template>
    
    <div id="wrapper">

        <nav class="px-4 py-6 flex items-stretch">
            <a href="http://localhost:8000/admin" class="text-blue-700 pr-4">Admin Site</a>
            <NuxtLink to="/"><a class="text-blue-700 pr-4">Home</a></NuxtLink>
        
            <form class="text-right" v-if="$auth.loggedIn" @submit.prevent="logout">
                <span class="pr-4">Welcome, <strong>{{ $auth.user.username }}</strong></span>
                <button type="submit" class="bg-gray-200 text-black px-3 py-1 rounded-full">Log Out</button>
            </form>

        </nav>

        <main class="p-4">
            <Nuxt />
        </main>

    </div>

</template>