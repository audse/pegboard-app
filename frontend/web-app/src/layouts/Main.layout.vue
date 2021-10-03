<script lang="ts" setup>

import Navbar from './Navbar.layout.vue'
import Sidebar from './Sidebar.layout.vue'

</script>
<template>

<div class="drawer drawer-mobile h-full">
    <input id="sidebar" type="checkbox" class="drawer-toggle"> 

    <div class="drawer-content">

        <navbar>
            <input id="sidebar" type="checkbox" class="drawer-toggle" />
            <label for="sidebar" class="drawer-button lg:hidden">
                <i class="gg-menu text-lg text-scale-text-4"></i>
            </label>
        </navbar>
        
        <main>
            <slot></slot>
        </main>

        <footer class="h-40">
        </footer>

    </div> 

    <div class="drawer-side shadow-sm h-full">
        <label for="sidebar" class="drawer-overlay"></label> 
        <sidebar class="shadow" />
    </div>

</div>

</template>
<script lang="ts">

export default {
    name: 'MainLayout'
}

</script>