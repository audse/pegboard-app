<template>
    
<article class="bg-gray-700 p-2 m-2">

{{ note.name }}

</article>

</template>
<script lang="ts">

export default {
    
    name: 'ViewNote',

    props: {
        note:Object,
    },

    setup () {

    }
}

</script>
