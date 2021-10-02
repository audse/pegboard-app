import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class BoardService extends Service {

    boardForm = {
        name: '',
        folder: undefined
    }

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

}

export default new BoardService()