<template>

<article class="border border-gray-300 p-3 m-3">
    {{ folder.name }}

    <section v-for="board in folder.boards" :key="board.id" class="border border-gray-300 p-3 m-5">
        {{ board.name }}
    </section>

    <form @submit.prevent="addBoard(addBoardForm, folder.id)">
        <label for="name">Board Name</label>
        <input v-model="addBoardForm.name" name="name" type="text" />
        <button type="submit">Add Board</button>
    </form>
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