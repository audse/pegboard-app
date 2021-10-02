import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class FolderService extends Service {

    folderForm = {
        name: ''
    }

    constructor () {
        super('folders')
    }

}

export default new FolderService()