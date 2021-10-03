
interface AuthState {
    currentUser:object|null,
    token:string,
    preferences:{
        sidebarHidden:boolean,
    }
}

const authStore = {
    namespaced: true,
    
    state () {
        return {
            currentUser: null,
            token: '',
            preferences: {
                sidebarHidden: false,
            }
        }
    },

    getters: {

        isAuthenticated: ( state:AuthState ) => {
            return state.currentUser !== null
        }

    },

    mutations: {

        setToken: ( state:AuthState, newToken:string ) => {
            state.token = newToken
        },

        setCurrentUser: ( state:AuthState, newUser:object ) => {
            state.currentUser = newUser
        },

        setSidebarHiddenPreference: ( state:AuthState, preference:boolean ) => {
            state.preferences.sidebarHidden = preference
        }

    },

}

export default authStore
