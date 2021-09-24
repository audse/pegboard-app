<template>
    
<section class="pt-6">
    <h3>Edit {{ page.name }}</h3>
    <form @submit.prevent="editPage(page.id, editPageForm)">
        <label for="name">Page Name</label>
        <input v-model="editPageForm.name" name="name" type="text" />
        <button type="submit">Submit</button>
    </form>
</section>

</template>

<script lang="ts">

import { computed } from 'vue'

import usePage from './../../../mixins/usePage'

export default {

    name: 'EditPage',

    props: {
        page: Object,
    },

    setup ( props:{page:object} ) {

        const {
            editPage
        } = usePage()

        const editPageForm = computed( () => Object.assign({}, props.page))

        return {
            editPage,
            editPageForm,
        }

    }
}

</script>