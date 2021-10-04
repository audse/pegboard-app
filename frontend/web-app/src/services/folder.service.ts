import axios, { AxiosRequestConfig } from 'axios'
import store from '../store'
import Service from './generic.service'

class FolderService extends Service {

    constructor () {
        super('folders')
    }

}

export default new FolderService()