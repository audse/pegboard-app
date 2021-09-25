
interface note {
    page:string,
    id:string,
}

interface noteState { 
    notes: Array< { page:string, notes:Array<note> } >
}

const noteStore = {
    namespaced: true,

    state () {
        return {
            notes: []
        }
    },
    
    getters: {

        getByPage ( state:noteState, pageId:string ) {
            const pageIndex = state.notes.findIndex( (page:any) => page.page === pageId )
            if ( pageIndex !== -1 ) {
                return state.notes[pageIndex].notes
            } throw new Error('Page not found.')
        },

        getById ( state:noteState, pageId:string='unsorted', noteId:string ) {
            const pageIndex = state.notes.findIndex( (page:any) => page.page === pageId )
            if ( pageIndex !== -1 ) {
                const noteIndex = state.notes[pageIndex].notes.findIndex( note => note.id === noteId )
                if ( noteIndex !== -1 ){
                    return state.notes[pageIndex].notes[noteIndex]
                } else throw new Error('Note not found.')
            } else throw new Error('Page not found.')
        }

    },

    mutations: {

        setByPage ( state:noteState, data:{pageId:string, notes:Array<note>} ) {
            state.notes.push({ page: data.pageId, notes: data.notes })
        },

        create ( state:noteState, noteData:note ) {
            const pageId = noteData.page ? noteData.page : 'unsorted'
            const pageIndex = state.notes.findIndex( (page:any) => page.page === pageId )
            if ( pageIndex !== -1 ) {
                state.notes[pageIndex].notes.push(noteData)
            }
        }

    }
}

export default noteStore