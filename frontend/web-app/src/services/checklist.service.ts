import axios, { AxiosRequestConfig } from 'axios'
import Service from './index.service'

class ChecklistService extends Service {

    constructor () {
        super('checklists')
    }

}

export default new ChecklistService()