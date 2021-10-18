<script lang="ts" setup>

import { NavbarLayout, SidebarLayout } from '@/layouts'

</script>
<template>

<div class="drawer drawer-mobile h-full">

    <input id="sidebar-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content" id="page-root">

        <navbar-layout>
            <label for="sidebar-drawer" class="lg:hidden drawer-button w-auto">
                <span class=" block subtle-text rounded-lg px-2 py-4">
                    <i class="gg-menu icon-lg text-scale-text-4"></i>
                </span>
            </label>
        </navbar-layout>
        
        <main>
            <slot></slot>
        </main>


    </div> 

    <div class="drawer-side shadow-sm h-full">
        <label for="sidebar-drawer" class="drawer-overlay"></label> 
        <sidebar-layout class="shadow" />
    </div>

</div>

</template>
<script lang="ts">

export default {
    name: 'main-layout'
}

</script>