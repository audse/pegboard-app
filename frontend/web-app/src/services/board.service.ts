import axios, { AxiosRequestConfig } from 'axios'

import store from '@/store'
import { Folder } from '@/types'
import Service from './generic.service'


class BoardService extends Service {
    
    constructor () {
        super('boards')
    }
    
    async listUnsorted () {
        try {
            const response = await axios.get(`${this.url}unsorted/`, this.config)
            store.commit(`${this.storeName}/set`, response.data)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async createInFolder (data:object, folder:Folder) {
        try {
            const response:{data:object} = await axios.post(this.url, data=data, this.config)
            const folderState = store.getters['folders/getById'](folder.id)
            folderState.boards.push(response.data)
            store.commit(`folders/update`, folderState)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

}

export default new BoardService()