import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class BoardService extends Service {

    constructor () {
        super('boards')
    }

    async listUnsorted () {
        try {
            return await axios.get(`${this.url}unsorted/`)
        } catch (e:any) {
            throw e
        }
    }

}