
interface board {
    folder:string,
    id:string,
}

interface boardState { 
    boards: Array< { folder:string, boards:Array<board> } >
}

const boardStore = {
    namespaced: true,

    state () {
        return {
            boards: []
        }
    },
    
    getters: {

        getByFolder: (state:boardState) => (folderId:string) => {
            const folderIndex = state.boards.findIndex( (folder:any) => folder.folder === folderId )
            if ( folderIndex !== -1 ) {
                return state.boards[folderIndex].boards
            }
        },

        getById: (state:boardState) => (folderId:string='unsorted', boardId:string) => {
            const folderIndex = state.boards.findIndex( (folder:any) => folder.folder === folderId )
            if ( folderIndex !== -1 ) {
                const boardIndex = state.boards[folderIndex].boards.findIndex( board => board.id === boardId )
                if ( boardIndex !== -1 ){
                    return state.boards[folderIndex].boards[boardIndex]
                }
            }
        }

    },

    mutations: {

        setByFolder ( state:boardState, folderData:{folder:string, boards:Array<board>} ) {
            const folderIndex = state.boards.findIndex( (folder:any) => folder.folder === folderData.folder )
            if ( folderIndex !== -1 ) {
                state.boards[folderIndex] = folderData
            } else {
                state.boards.push(folderData)
            }
        },

        create ( state:boardState, boardData:board ) {
            const folderId = boardData.folder ? boardData.folder : 'unsorted'
            const folderIndex = state.boards.findIndex( (folder:any) => folder.folder === folderId )
            if ( folderIndex !== -1 ) {
                state.boards[folderIndex].boards.push(boardData)
            }
        }

    }
}

export default boardStore