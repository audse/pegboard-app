import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class FolderService extends Service {

    constructor () {
        super('folders')
    }

}

export default new FolderService()