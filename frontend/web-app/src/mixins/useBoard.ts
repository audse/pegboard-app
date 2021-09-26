
import { reactive, ref } from 'vue'
import BoardService from '../services/board.service'

const useBoard = () => {

    const unsortedBoards:{value:Array<object>|null} = ref(null) 

    const refreshUnsortedBoards = async () => {
        BoardService.listUnsorted().then( (response:{data:Array<object>}) => {
            unsortedBoards.value = response.data
        }).catch((e:any) => {
            unsortedBoards.value = []
        })
    }

    let board = ref({})
    const refreshBoard = async (boardId:string) => {
        BoardService.retrieveBoardAndChildren(boardId).then( (response:{data:object}) => {
            board.value = response.data
        })
    }

    interface boardForm {
        name:string,
        folder:number|undefined
    }
    
    const refreshParent:{value:boolean} = ref(false)

    let addBoardForm:boardForm = reactive({...BoardService.boardForm})
    const addBoard = async (data:boardForm, folderId=undefined) => {
        data.folder = folderId
        await BoardService.create(data)
    }

    const editBoard = async (boardId: string, data:boardForm) => {
        await BoardService.update(boardId, data)
    }

    // const pages = ref()
    // const refreshPages = async (boardId:string) => {
    //     BoardService.listChildren(boardId).then( (response:{data:Array<object>}) => {
    //         pages.value = response.data
    //     }).catch( (e:any) => {
    //         pages.value = []
    //     })
    // }

    // let notes = ref()
    // const refreshNotes = async (boardId:string, pageId:string) => {
    //     BoardService.listGrandchildren(boardId, pageId).then( (response:{data:Array<object>}) => {
    //         notes.value = response.data
    //     }).catch( (e:any) => {
    //         notes.value = []
    //     })
    // }

    return {
        unsortedBoards,
        refreshUnsortedBoards,
        refreshParent,

        board,
        refreshBoard,

        addBoardForm,
        addBoard,

        editBoard,

        // pages,
        // refreshPages,

        // notes,
        // refreshNotes
    }

}

export default useBoard