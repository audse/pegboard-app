import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class FolderService extends Service {

    folderForm = {
        name: ''
    }

    constructor () {
        super('folders')
    }

    async listChildren (folderId:number) {
        try {
            return await axios.get(`${this.url}${folderId}/boards/`, this.config)
        } catch (e:any) {
            throw e
        }
    }

}

export default new FolderService()