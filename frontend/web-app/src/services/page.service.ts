import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class PageService extends Service {

    pageForm = {
        name: '',
        board: undefined
    }

    constructor () {
        super('pages')
    }

    // async listChildren (boardId:string) {
    //     try {
    //         return await axios.get(`${this.url}${boardId}/pages/`, this.config)
    //     } catch (e:any) {
    //         throw e
    //     }
    // }

}

export default new PageService()