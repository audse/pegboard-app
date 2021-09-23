
import { reactive, ref } from 'vue'
import FolderService from '../services/folder.service'
import BoardService from '../services/board.service'

const useBoard = () => {

    const unsortedBoards:any = ref(null) 

    const refreshUnsortedBoards = async () => {
        BoardService.listUnsorted().then( (response:{data:Array<object>}) => {
            unsortedBoards.value = response.data
        }).catch((e:any) => {
            console.log(e)
            unsortedBoards.value = {}
        })
    }

    interface boardForm {name:string, folder:number|undefined}

    let addBoardForm:boardForm = reactive({...BoardService.boardForm})
    const addBoard = async (data:boardForm, folderId=undefined) => {
        if (folderId !== undefined) data.folder = folderId
        BoardService.create(data).then( () => {
            refreshUnsortedBoards() // TODO switch to `pushToFolder` ?
        }).catch((e:any) => console.log(e) )
    }

    return {
        unsortedBoards,
        refreshUnsortedBoards,

        addBoardForm,
        addBoard
    }

}

export default useBoard