import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Service from './index.service'

class NoteService extends Service {

    noteForm = {
        name: '',
        board: undefined,
        page: undefined
    }

    constructor () {
        super('notes')
    }

}

export default new NoteService()