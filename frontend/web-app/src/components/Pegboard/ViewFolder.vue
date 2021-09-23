<template>

<article class="bg-gray-800 p-3 m-3">
    <h2>{{ folder.name }}</h2>

    <form @submit.prevent="addBoard(addBoardForm, folder.id)">
        <label for="name">Board Name</label>
        <input v-model="addBoardForm.name" name="name" type="text" />
        <button type="submit">Add Board</button>
    </form>

    <section v-for="board in folder.boards" :key="board.id" class="bg-gray-700 p-3 m-5">
        {{ board.name }}
    </section>

</article>

</template>
<script lang="ts">

import { onMounted, watch } from 'vue'
import useFolder from '../../mixins/useFolder'
import useBoard from '../../mixins/useBoard'

export default {
    name: 'ViewFolder',

    props: {
        folder: Object
    },
    
    setup ( props:{folder:object} ) {

        const {
            refreshChildrenOf,
        } = useFolder()

        const {
            addBoardForm,
            addBoard
        } = useBoard()

        onMounted( () => {
            refreshChildrenOf(props.folder)
        })

        watch( props.folder, (() => {
            refreshChildrenOf(props.folder)
        }))

        return {
            addBoardForm,
            addBoard
        }

    }
}

</script>