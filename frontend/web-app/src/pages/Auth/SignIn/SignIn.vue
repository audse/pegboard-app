<template>


<form @submit.prevent="signIn(signInData)">

<section>
    <label for="username">Username</label>
    <input v-model="signInData.username" name="username" type="text" />
</section>
<section>
    <label for="password">Password</label>
    <input v-model="signInData.password" name="password" type="password" />
</section>
<section>
    <button type="submit">Sign In</button>
</section>

</form>

<label>Not signed up?</label>
<router-link :to="{ name: 'Sign Up' }">
    <button class="secondary">Sign Up</button>
</router-link>


</template>
<script lang="ts">

import { reactive, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import AuthService from './../../../services/auth.service'

export default {

    setup () {

        const router = useRouter()

        const signInData = reactive({
            username: '',
            password: '',
        })

        const auth = new AuthService()

        const signIn = async ( data:object ) => {
            await auth.signIn( data ).then( (userResponse:object) => {
                router.push({ name: 'Home' })
            }).catch( (e:any) => {
                throw e
            })
        }

        return {
            signInData,
            signIn
        }

    }

}

</script>