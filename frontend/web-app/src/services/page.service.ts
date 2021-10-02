import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class PageService extends Service {

    constructor () {
        super('pages')
    }

}

export default new PageService()