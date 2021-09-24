
interface folderState { 
    folders:Array<object>
}

const folderStore = {
    namespaced: true,

    state () {
        return {
            folders: []
        }
    },
    
    getters: {

        getById ( state:folderState, folderId:string ) {
            const folderIndex = state.folders.findIndex( (storeFolder:any) => storeFolder.id === folderId )
            if ( folderIndex != -1 ) {
                return state.folders[folderIndex]
            }
        }

    },

    mutations: {

        set ( state:folderState, list:Array<object> ) {
            state.folders = list
        },

        create ( state:folderState, folder:object ) {
            state.folders.push(folder)
        },

        update ( state:folderState, folder:object ) {
            const folderIndex = state.folders.findIndex( (storeFolder:any) => storeFolder.id === folder.id )
            if ( folderIndex != -1 ) {
                state.folders.splice(folderIndex, 1).push(folder)
            }
        },

    }
}

export default folderStore