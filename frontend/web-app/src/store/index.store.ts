import { createStore } from 'vuex'

import auth from './auth.store'

const store = createStore({
    
    modules: {
        auth
    }

})

export default store