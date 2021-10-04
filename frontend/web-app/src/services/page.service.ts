import axios, { AxiosRequestConfig } from 'axios'
import store from '../store'
import Service from './generic.service'

class PageService extends Service {

    constructor () {
        super('pages')
    }

}

export default new PageService()