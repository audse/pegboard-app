import { createStore } from 'vuex'

import auth from './auth.store'
import folders from './folder.store'
import boards from './board.store'

const store = createStore({
    
    modules: {
        auth,
        folders,
        boards,
    }

})

export default store