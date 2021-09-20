<template>
<!--
<div id="g_id_onload"
    data-client_id="652460956969-394v9crnmp6hf9pugt6vua5vsrin5odr.apps.googleusercontent.com"
    data-callback="signUpWithGoogle">
</div>
<div class="g_id_signin"
    data-ux_mode="redirect"
    data-type="standard"
    data-size="large"
    data-theme="outline"
    data-text="sign_in_with"
    data-shape="rectangular"
    data-logo_alignment="left">
</div>
-->

<div id="googleLogin"></div>

<form @submit.prevent="signUpWithEmail(signUpData)">
<section>
    <label for="username">Username</label>
    <input v-model="signUpData.username" name="username" type="text" />
</section>
<section>
    <label for="email">Email</label>
    <input v-model="signUpData.email" name="email" type="email" />
</section>
<section>
    <label for="password">Password</label>
    <input v-model="signUpData.password1" name="password" type="password" />
</section>
<section>
    <label for="confirmPassword">Confirm Password</label>
    <input v-model="signUpData.password2" name="confirmPassword" type="password" />
</section>
<section>
    <button type="submit">Sign Up</button>
</section>
</form>

<label>Already signed up?</label>
<router-link :to="{ name: 'Sign In' }">
    <button class="secondary">Sign In</button>
</router-link>


</template>

<script lang="ts">

import { reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AuthService from './../../../services/auth.service'

export default {
    name: 'SignUp', 
    setup () {

        const router = useRouter()

        const signUpData = reactive({
            username: '',
            email: '',
            password1: '',
            password2: '',
        })

        const signUpWithEmail = async ( data:object ) => {
            AuthService.signUpWithEmail( data ).then( (response:object) => {
                router.push({ name: 'Sign Up Success' })
            }).catch( (e:any) => {
                throw e
            })
        }

        const signUpWithGoogle = ( response:any ) => {
            console.log('Signing in with google...', response)
            AuthService.signUpWithGoogle(response.credential)
        }

        const initializeGoogle = () => {

            google.accounts.id.initialize({
                client_id: '652460956969-394v9crnmp6hf9pugt6vua5vsrin5odr.apps.googleusercontent.com',
                login_uri: 'http://localhost:8000/api/auth/google/'
            })

            google.accounts.id.renderButton(
                document.getElementById('googleLogin'),
                { theme: "outline", size: "large" }  // customization attributes
            )
        }

        onMounted(initializeGoogle)

        return {
            signUpData,
            signUpWithEmail,
        }
    }
}

</script>