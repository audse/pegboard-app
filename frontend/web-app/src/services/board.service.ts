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

    // async listChildren (boardId:string) {
    //     try {
    //         const response:{data:Array<object>} = await axios.get(`${this.url}${boardId}/pages/`, this.config)
    //         store.commit(`pages/set`, response.data)
    //         return response.data
    //     } catch (e:any) {
    //         throw e
    //     }
    // }

    // async listGrandchildren (boardId:string, pageId:string) {
    //     try {
    //         const response:{data:Array<object>} = await axios.get(`${this.url}${boardId}-${pageId}/notes/`, this.config)
    //         store.commit('notes/setByPage', { pageId: pageId, data: response.data })
    //         return response.data
    //     } catch (e:any) {
    //         throw e
    //     }
    // }

}

export default new BoardService()