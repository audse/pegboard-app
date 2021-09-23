
import { reactive, ref } from 'vue'
import NoteService from '../services/note.service'

const useNote = () => {

    let note = ref({})
    const refreshNote = async (noteId:string) => {
        NoteService.retrieve(noteId).then( (response:{data:object}) => {
            note.value = response.data
        })
    }

    interface noteForm {
        name:string,
        board:number|undefined,
        page:number|undefined,
    }

    let addNoteForm:noteForm = reactive({...NoteService.noteForm})
    const addNote = async (data:noteForm, boardId=undefined, pageId=undefined) => {
        data.board = boardId
        data.page = pageId
        await NoteService.create(data)
    }

    return {
        note,
        refreshNote,

        addNoteForm,
        addNote,
    }

}

export default useNote