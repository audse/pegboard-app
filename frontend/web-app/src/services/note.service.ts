import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class NoteService extends Service {

    constructor () {
        super('notes')
    }

}

export default new NoteService()