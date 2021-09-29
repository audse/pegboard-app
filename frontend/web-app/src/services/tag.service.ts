import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class TagService extends Service {

    constructor () {
        super('tags')
    }

}

export default new TagService()