import { createStore } from 'vuex'

import auth from './auth.store'

import {
    folders,
    boards,
    pages,
    notes,

    colors, 
    tags, 
    checklists, 
    comments,

} from './generic.store'

const store = createStore({
    
    modules: {
        auth,

        folders,
        boards,
        pages,
        notes,

        colors,
        tags,
        checklists,
        comments
    }

})

export default store