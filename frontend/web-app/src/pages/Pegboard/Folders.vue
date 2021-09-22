<template>

{{ folders }}

</template>
<script lang="ts">

import { computed } from 'vue'

import FolderService from './../../services/folder.service'

export default {
    name: 'Folders',

    setup () {

        const folders = computed( () => {
            FolderService.list().then( (response:array) => {
                console.log(response)
                return response
            }).catch( (e:any) => {
                console.log(e)
                return []
            })
        })

        return {
            folders
        }

    }
}


</script>