
interface AuthState {
    currentUser:object|null,
    token:string,
}

const authStore = {
    namespaced: true,
    
    state () {
        return {
            currentUser: null,
            token: '',
        }
    },

    getters: {

        isAuthenticated ( state:AuthState ) {
            return state.currentUser !== null
        }

    },

    mutations: {

        setToken ( state:AuthState, newToken:string ) {
            state.token = newToken
        },

        setCurrentUser ( state:AuthState, newUser:object ) {
            state.currentUser = newUser
        }

    },

}

export default authStore
