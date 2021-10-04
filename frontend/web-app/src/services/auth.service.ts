import axios from 'axios'
import store from '../store'
import Service from './generic.service'

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

    constructor () {
        super('auth')
    }

    async signUpWithEmail ( data:SignUpData ) {
        try {
            return await axios.post(`${this.url}signup/`, data, this.config)
        } catch (e:any) {
            throw e
        }
    }

    async signIn ( data:SignInData ) {
        try {
            const requestData:any = await axios.post(`${this.url}login/`, data)
            const token:string = requestData.data.key
            return await this.loadCurrentUser(token)
        } catch (e:any) {
            throw e
        }
    }

    async signOut () {
        try {
            await axios.post(`${this.url}logout/`, this.config)
            this.updateStore('', null)
            return
        } catch (e:any) {
            throw e
        }
    }

    async loadCurrentUser ( token:string='' ) {
        const authToken:string = token || localStorage.getItem('token') || 'null'

        if ( authToken !== 'null' ) {

            this.config.headers['Authorization'] = `Token ${authToken}`

            try {
                // Get user data
                const requestData = await axios.get(`${this.url}user/`, this.config)
                const currentUser = requestData.data

                // Update storage
                this.updateStore( authToken, currentUser )

                // Return current user
                return currentUser
            } catch (e:any) {
                throw e
            }
        } else return null
    }

    updateStore ( token:string, currentUser:object|null ) {
        localStorage.setItem('token', token)
        store.commit('auth/setToken', token)
        store.commit('auth/setCurrentUser', currentUser)
    }

    // TODO class-specific methods
    // [ ] forgot password
    // [ ] forgot email
    // [ ] forgot username

}

export default new AuthService()