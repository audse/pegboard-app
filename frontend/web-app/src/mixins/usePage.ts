
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

    // const pages = ref([])
    // const refreshChildren = async (pageId:string) => {
    //     PageService.listChildren(pageId).then( (response:{data:Array<object>}) => {
    //         pages.value = response.data
    //     }).catch( (e:any) => {
    //         pages.value = []
    //     })
    // }

    return {
        page,
        refreshPage,

        // pages,
        // refreshChildren,

        addPageForm,
        addPage
    }

}

export default usePage