
import { computed, reactive, ref } from 'vue'
import FolderService from '../services/folder.service'
import { useStore } from 'vuex'

const useFolder = () => {

    const store = useStore()

    const folders:any = computed( () => store.state.folders.folders )
    const boards:any = computed( () => store.state.boards.boards )

    const refreshFolders = async () => {
        await FolderService.list()
    }

    const refreshChildren = async () => {
        folders.value.map( (folder:any) => {
            // listChildren(folder.id)
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