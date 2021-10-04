import axios, { AxiosRequestConfig } from 'axios'
import store from '../store'
import Service from './generic.service'

class TagService extends Service {

    constructor () {
        super('tags')
    }

}

export default new TagService()