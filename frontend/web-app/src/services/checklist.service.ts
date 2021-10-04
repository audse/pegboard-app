import axios, { AxiosRequestConfig } from 'axios'
import Service from './generic.service'

class ChecklistService extends Service {

    constructor () {
        super('checklists')
    }

}

export default new ChecklistService()