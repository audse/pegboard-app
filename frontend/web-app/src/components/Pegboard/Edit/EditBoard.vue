<template>
    
<section class="pt-6">
    <h3>Edit {{ board.name }}</h3>
    <form @submit.prevent="editBoard(board.id, editBoardForm)">
        <label for="name">Board Name</label>
        <input v-model="editBoardForm.name" name="name" type="text" />
        <button type="submit">Submit</button>
    </form>
</section>

</template>

<script lang="ts">

import { computed, reactive } from 'vue'

import useBoard from './../../../mixins/useBoard'

export default {

    name: 'EditBoard',

    props: {
        board: Object,
    },

    setup ( props:{board:object} ) {

        const {
            editBoard
        } = useBoard()

        const editBoardForm = computed( () => Object.assign({}, props.board))

        return {
            editBoard,
            editBoardForm,
        }

    }
}

</script>