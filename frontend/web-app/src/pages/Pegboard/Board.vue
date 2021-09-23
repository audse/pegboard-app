<template>
    
<article v-if="board">

<h1>{{ board.name }}</h1>
<h2>{{ board.description }}</h2>

<section>
    <form @submit.prevent="addPage(addPageForm, board.id)">
        <label for="name">Page Name</label>
        <input v-model="addPageForm.name" name="name" type="text" />
        <button type="submit">Add Page</button>
    </form>
</section>

<section v-for="page in pages" :key="page.id" class="flex">
    <view-page :page="page" />
</section>

</article>

</template>

<script components:{ViewPage} lang="ts" setup>

import ViewPage from '../../components/Pegboard/ViewPage.vue'

import { onMounted, reactive } from 'vue'
import { useRoute } from 'vue-router'

import useBoard from './../../mixins/useBoard'
import usePage from './../../mixins/usePage'

const route = useRoute()

const {
    board,
    refreshBoard,

    pages,
    refreshChildren
} = useBoard()

const id = route.params.id.toString()

onMounted( () => {
    refreshBoard(id)
    refreshChildren(id)
})

const {
    page,
    refreshPage,

    addPageForm,
    addPage
} = usePage()

</script>