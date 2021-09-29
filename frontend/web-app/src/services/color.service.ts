import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class ColorService extends Service {

    constructor () {
        super('colors')
    }

}

export default new ColorService()