import axios from 'axios'
import { useStore } from 'vuex'
import Service from './index.service'

interface SignUpData {
    username:string,
    email:string,
    password1:string,
    password2:string,
}

interface SignInData {
    username:string,
    password:string,
}

class AuthService extends Service {

    store:any = useStore()

    constructor () {
        super('auth')
    }

    async signUpWithEmail ( data:SignUpData ) {
        try {
            return await axios.post(`${this.url}signup/`, data)
        } catch (e:any) {
            throw e
        }
    }

    async signIn ( data:SignInData ) {
        try {
            const requestData:any = await axios.post(`${this.url}login/`, data)
            const token:string = requestData.data.key
            return await this.setCurrentUser(token)
        } catch (e:any) {
            throw e
        }
    }

    async setCurrentUser ( token:string ) {
        const authConfig = { headers: { 'Authorization': `Token ${token}` } }

        try {
            // Get user data
            const requestData = await axios.get(`${this.url}user/`, authConfig)
            const currentUser = requestData.data

            // Update storage
            this.updateStore( token, currentUser )

            // Return current user
            return currentUser
        } catch (e:any) {
            throw e
        }
    }

    updateStore ( token:string, currentUser:object|null ) {
        localStorage.setItem('token', token)
        this.store.commit('auth/setToken', token)
        this.store.commit('auth/setCurrentUser', currentUser)
    }

    // TODO class-specific methods
    // [ ] forgot password
    // [ ] forgot email
    // [ ] forgot username

}

export default AuthService