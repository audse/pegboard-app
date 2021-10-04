import axios, { AxiosRequestConfig } from 'axios'
import store from '../store'
import Service from './generic.service'

class ColorService extends Service {

    constructor () {
        super('colors')
    }

}

export default new ColorService()