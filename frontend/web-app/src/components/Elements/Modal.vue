<script lang="ts" setup>

const props = defineProps({
    show: Boolean,
})

const emits = defineEmits([
    'hide'
])

const hideModal = (event:any) => {
    if ( event.target.className === 'overlay' ) {
        emits('hide')
    }
}

</script>

<template>
    
<div class="overlay" v-show="show" @click="hideModal">
    <article>
        <slot></slot>
    </article>
</div>

</template>
<script lang="ts">

export default {
    name: 'Modal'
}

</script>
<style scoped>

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0,0,0,0.4);
    isolation: isolate;
}

article {

    @apply px-6 py-12;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 75vw;
    height: 50vh;
    background: var(--secondary);
    overflow-y: scroll;
}

</style>