
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
        BoardService.retrieve(boardId).then( (response:{data:object}) => {
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

    const pages = ref([])
    const refreshChildren = async (boardId:string) => {
        BoardService.listChildren(boardId).then( (response:{data:Array<object>}) => {
            pages.value = response.data
        }).catch( (e:any) => {
            pages.value = []
        })
    }

    return {
        unsortedBoards,
        refreshUnsortedBoards,
        refreshParent,

        board,
        refreshBoard,

        pages,
        refreshChildren,

        addBoardForm,
        addBoard
    }

}

export default useBoard