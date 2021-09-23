
<template>

<article class="bg-gray-800 p-3 m-3">

    <section>
        <strong>{{ page.name }}</strong>
        {{ page.description }}
    </section>
    
</article>

</template>
<script lang="ts">

export default {

    name: 'ViewPage',

    props: {
        page:Object,
    },

}

</script>