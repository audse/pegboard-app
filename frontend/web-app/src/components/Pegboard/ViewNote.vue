<template>
    
<article class="bg-gray-700 p-2 m-2">

{{ note.name }}

<edit-note :note="note" />

</article>

</template>
<script lang="ts">
import EditNote from './Edit/EditNote.vue'

export default {
    
    name: 'ViewNote',

    props: {
        note:Object,
    },

    components: { 
        EditNote
    },
    
    setup () {

    }
}

</script>
