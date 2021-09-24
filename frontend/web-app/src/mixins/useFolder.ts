
import { reactive, ref } from 'vue'
import FolderService from '../services/folder.service'

const useFolder = () => {

    const folders:any = ref(null) 

    const refreshFolders = async () => {
        FolderService.list().then( (response:{data:Array<object>}) => {
            folders.value = response.data
        }).catch((e:any) => console.log(e))
    }

    const refreshChildren = async () => {
        folders.value.map( (folder:any) => {
            listChildren(folder.id).then( (response:any) => {
                console.log(response)
                folder.boards = response
            })
        })
    }

    const refreshChildrenOf = async (folder:any) => {
        listChildren(folder.id).then( (response:any) => {
            folder.boards = response
        })
    }

    const listChildren = async (folderId:number) => {
        return new Promise( (resolve) => {
            FolderService.listChildren(folderId).then( (response:{data:object}) => {
                resolve(response.data)
            }).catch( (e:any) => console.log(e) )
        })
    }

    interface folderForm {name:string}

    let addFolderForm:folderForm = reactive({...FolderService.folderForm})
    const addFolder = async (data:folderForm) => {
        await FolderService.create(data)
    }

    const editFolder = async (folderId:string, data:folderForm) => {
        await FolderService.update(folderId, data)
    }

    return {
        folders,
        refreshFolders,
        refreshChildren,
        refreshChildrenOf,

        addFolderForm,
        addFolder,

        editFolder
    }
}

export default useFolder