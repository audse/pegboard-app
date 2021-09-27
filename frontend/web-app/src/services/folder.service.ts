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

    async listWithChildren () {
        try {
            const response:{data:Array<object>} = await axios.get(`${this.url}boards/all/`, this.config)
            store.commit('folders/set', response.data)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

}

export default new FolderService()