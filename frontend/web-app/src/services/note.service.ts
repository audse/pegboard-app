import axios, { AxiosRequestConfig } from 'axios'
import store from '../store'
import Service from './generic.service'

class NoteService extends Service {

    constructor () {
        super('notes')
    }

}

export default new NoteService()