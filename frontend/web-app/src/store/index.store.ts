import { createStore } from 'vuex'

import auth from './auth.store'
import folders from './folder.store'
import boards from './board.store'
import pages from './page.store'
import notes from './note.store'

const store = createStore({
    
    modules: {
        auth,
        folders,
        boards,
        pages,
        notes
    }

})

export default store