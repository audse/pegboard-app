<script lang="ts" setup>

import { computed, ref } from 'vue'
import { useStore } from 'vuex'


const props = defineProps({
    show:Boolean,
    tabs:Array,
})

const emits = defineEmits([
    'hide'
])

const hideModal = (event:any) => {
    if ( event.target.className === 'overlay' || event.target.className.includes('wrapper') ) {
        emits('hide')
    }
}

const activeTab = ref(props.tabs ? props.tabs[0] : '')

// Calculate modal width depending on screen size and sidebar visibility
const store = useStore()
const sidebarHidden = computed( () => store.state.auth.preferences.sidebarHidden )


</script>

<template>
    
<div :class="['co-modal-wrapper text-text no-scrollbar', !show?'h-0 w-0':'w-full h-full']">
    <div :class="['overlay', !show?'hidden':'']" @click="hideModal"></div>

    <transition name="translate-fade">
        <card bg="main" :class="['co-modal', !sidebarHidden?'left-16 lg:left-80':'left-16']" v-show="show" @click="hideModal">

            <template #header>
                <slot name="header" />

                <toolbar>
                <label v-for="tab of tabs" :key="`label-${tab}`">
                    <slot :name="`label-${tab}`">
                        <co-button @click="activeTab=tab" :color="tab===activeTab?'emphasis':'scale-text-500'" :subtle="tab!==activeTab" :light="tab==activeTab" class="mr-1">
                            {{ tab }}
                        </co-button>
                    </slot>
                </label>
                </toolbar>
            </template>

            <slot></slot>

            <section v-for="tab of tabs" :key="`section-${tab}`" class="pt-4">
                <article v-if="tab===activeTab">
                    <slot :name="`section-${tab}`" />
                </article>
            </section>

            <template #footer>
                <slot name="footer" />
            </template>
        </card>
    </transition>
</div>

</template>
<script lang="ts">

export default {
    name: 'Modal'
}

</script>
<style scoped>

.overlay {
    @apply px-4 pt-8 lg:pl-80;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background-color: rgba(0,0,0,0.4);
    z-index: 1000;
}

.co-modal-wrapper {
    overflow: hidden;
}

.co-modal {
    @apply top-8 bottom-8 right-8;
    position: fixed;
    z-index: 1001;
    max-height: 100%;
}

</style>