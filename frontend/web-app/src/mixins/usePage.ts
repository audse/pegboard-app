
import { reactive, ref } from 'vue'
import PageService from '../services/page.service'

const usePage = () => {

    let page = ref({})
    const refreshPage = async (pageId:string) => {
        PageService.retrieve(pageId).then( (response:{data:object}) => {
            page.value = response.data
        })
    }

    interface pageForm {
        name:string,
        board:number|undefined
    }

    let addPageForm:pageForm = reactive({...PageService.pageForm})
    const addPage = async (data:pageForm, boardId=undefined) => {
        data.board = boardId
        await PageService.create(data)
    }

    const editPage = async (pageId:string, data:pageForm) => {
        await PageService.update(pageId, data)
    }

    return {
        page,
        refreshPage,

        addPageForm,
        addPage,

        editPage,
    }

}

export default usePage