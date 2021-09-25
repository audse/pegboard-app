
interface pageState { 
    pages:Array<object>
}

const pageStore = {
    namespaced: true,

    state () {
        return {
            pages: []
        }
    },
    
    getters: {

        getById ( state:pageState, pageId:string ) {
            const pageIndex = state.pages.findIndex( (storePage:any) => storePage.id === pageId )
            if ( pageIndex != -1 ) {
                return state.pages[pageIndex]
            }
        }

    },

    mutations: {

        set ( state:pageState, list:Array<object> ) {
            state.pages = list
        },

        create ( state:pageState, page:object ) {
            state.pages.push(page)
        },

        update ( state:pageState, page:object ) {
            const pageIndex = state.pages.findIndex( (storePage:any) => storePage.id === page.id )
            if ( pageIndex != -1 ) {
                state.pages.splice(pageIndex, 1).push(page)
            }
        },

    }
}

export default pageStore