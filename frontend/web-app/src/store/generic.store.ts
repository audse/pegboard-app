
interface storeState {
    items:Array<object>,
    current:object,
}

const generic = {
    namespaced: true,

    state () {
        return {
            items: [],
            current: {},
        }
    },

    getters: {
        
        getById: ( state:storeState ) => ( id:number ) => {
            const index = state.items.findIndex( (storeItem:any) => storeItem.id === id )
            if ( index != -1 ) {
                return state.items[index]
            }
        }
    },

    mutations: {

        set: ( state:storeState, list:Array<object> ) => {
            state.items = list
        },

        setCurrent: ( state:storeState, item:object ) => {
            state.current = item
        },

        create: ( state:storeState, item:object ) => {
            state.items.push(item)
        },

        update: ( state:storeState, item:{id:number} ) => {
            const index = state.items.findIndex( (storeItem:any) => storeItem.id === item.id )
            if ( index != -1 ) {
                state.items.splice(index, 1).push(item)
            }
        },

        remove: ( state:storeState, id:number ) => {
            const index = state.items.findIndex( (storeItem:any) => storeItem.id === id )
            if ( index != -1 ) {
                state.items.splice(index, 1)
            }
        }
    }
}

const folders = {...generic}
const boards = {...generic}
const pages = {...generic}
const notes = {...generic}

const colors = {...generic}
const tags = {...generic}
const checklists = {...generic}
const comments = {...generic}
const themes = {...generic}

export {
    generic,

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