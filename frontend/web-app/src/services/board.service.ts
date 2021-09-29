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
            store.commit(`${this.storeName}/setByFolder`, { folder:'unsorted', boards:response.data })
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async retrieveBoardAndChildren (boardId:string) {
        try {
            const response:{data:object} = await axios.get(`${this.url}${boardId}/board/`, this.config)
            store.commit('boards/setCurrentBoard', response.data)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

}

export default new BoardService()