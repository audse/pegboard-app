<script lang="ts" setup>

import Navbar from './Navbar.layout.vue'
import Sidebar from './Sidebar.layout.vue'

</script>
<template>

<div class="drawer drawer-mobile h-full">

    <input id="sidebar-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">

        <navbar>
            <label for="sidebar-drawer" class="lg:hidden drawer-button w-auto">
                <span class=" block subtle-text rounded-lg px-2 py-4">
                    <i class="gg-menu icon-lg text-scale-text-4"></i>
                </span>
            </label>
        </navbar>
        
        <main>
            <slot></slot>
        </main>

        <footer class="h-40">
        </footer>

    </div> 

    <div class="drawer-side shadow-sm h-full">
        <label for="sidebar-drawer" class="drawer-overlay"></label> 
        <sidebar class="shadow" />
    </div>

</div>

</template>
<script lang="ts">

export default {
    name: 'MainLayout'
}

</script>