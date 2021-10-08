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
    themes

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
        comments,
        themes
    }

})

export default store