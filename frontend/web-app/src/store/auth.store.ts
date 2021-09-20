
interface AuthState {
    currentUser:object,
    token:string,
}

const authStore = {
    namespaced: true,
    
    state () {
        return {
            currentUser: Object(),
            token: '',
        }
    },

    getters: {

        isAuthorized ( state:AuthState ) {
            return state.currentUser ? true : false
        }

    },

    mutations: {

        setToken (state:AuthState, newToken:string) {
            state.token = newToken
        },

        setCurrentUser (state:AuthState, newUser:any) {
            state.currentUser = newUser
        }

    }

}

export default authStore
