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
<section>
    <label>Not signed up?</label>
    <button class="secondary" to="/signin/">Sign Up</button>
</section>

</form>

</template>
<script lang="ts">

import { reactive, computed, watch } from 'vue'
import { useStore } from 'vuex'
import AuthService from './../../../services/auth.service'

export default {

    setup () {

        const store = useStore()
        const user = computed( () => store.state.auth['currentUser'] )

        const signInData = reactive({
            username: '',
            password: '',
        })

        const auth = new AuthService()

        const signIn = async ( data:object ) => {
            await auth.signIn( data ).then( (userResponse:object) => {
                console.log(userResponse)
            })
        }

        return {
            user,
            signInData,
            signIn
        }

    }

}

</script>