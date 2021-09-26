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
            return await axios.get(`${this.url}unsorted/`, this.config)
        } catch (e:any) {
            throw e
        }
    }

    async retrieveBoardAndChildren (boardId:string) {
        try {
            return await axios.get(`${this.url}${boardId}/board/`, this.config)
        } catch (e:any) {
            throw e
        }
    }

}

export default new BoardService()