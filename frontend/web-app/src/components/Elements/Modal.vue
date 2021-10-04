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
    console.log(event.target.className)
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
    
<div class="co-modal-wrapper">
    <div :class="['overlay', !show?'hidden':'']" @click="hideModal"></div>

    <transition name="translate-fade">
        <card bg="primary" :class="['co-modal', !sidebarHidden?'left-16 lg:left-80':'left-16']" v-show="show" @click="hideModal">

            <template #header>
                <slot name="header" />

                <label v-for="tab of tabs" :key="`label-${tab}`">
                    <slot :name="`label-${tab}`">
                        <co-button @click="activeTab=tab" :color="tab===activeTab?'emphasis':'scale-text-500'" :subtle="tab!==activeTab" :light="tab==activeTab">
                            {{ tab }}
                        </co-button>
                    </slot>
                </label>
            </template>

            <slot></slot>

            <section v-for="tab of tabs" :key="`section-${tab}`">
                <transition name="scale" mode="out-in">
                    <article v-if="tab===activeTab">
                        <slot :name="`section-${tab}`">
                            ...
                        </slot>
                    </article>
                </transition>
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
    @apply px-8 pt-16 lg:pl-80;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background-color: rgba(0,0,0,0.4);
    z-index: 1000;
}

.co-modal {
    @apply top-16 bottom-16 right-16;
    position: fixed;
    z-index: 1001;
    overflow-y: scroll;
    overflow-x: hidden;
}

</style>