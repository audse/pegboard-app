<template>

<section v-if="folders && folders.length > 0">
{{ folders }}
</section>
<section v-else>
    No folders.
</section>

</template>
<script lang="ts">

import { computed } from 'vue'

import FolderService from './../../services/folder.service'

export default {
    name: 'Folders',

    setup () {

        interface responseObject {
            data:Array<object>
        }

        const folders = computed( () => {
            
            FolderService.list().then( (response:responseObject) => {
                console.log(response.data)
                return response.data
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