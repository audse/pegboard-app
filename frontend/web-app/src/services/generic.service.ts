import axios, { AxiosRequestConfig } from 'axios'
import store from '../store'
import Cookies from 'js-cookie'

import { GenericType } from '@/types'

type GenericRetrieveResponse = {
    data:GenericType
}

type GenericListResponse = {
    data:Array<GenericType>
}

class Service {
    
    url:string = 'http://localhost:8000/api/'
    store:any = store
    storeName:string = ''

    config:AxiosRequestConfig = {
        headers: {
            'X-CSRFToken': Cookies.get('csrftoken'),
            'Authorization': `Token ${localStorage.getItem('token')}`,
        },
        withCredentials: true,
    }

    constructor ( url:string ) {
        this.url = `${this.url}${url}/`
        this.storeName = url
    }

    async list () {
        try {
            const response:{data:Array<object>} = await axios.get(this.url, this.config)
            store.commit(`${this.storeName}/set`, response.data)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async retrieve ( pk:string|number ) {
        try {
            const response:GenericRetrieveResponse = await axios.get(`${this.url}${pk.toString()}/`, this.config)
            store.commit(`${this.storeName}/setCurrent`, response.data)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async create ( data:object ) {
        try {
            const response:{data:object} = await axios.post(this.url, data=data, this.config)
            store.commit(`${this.storeName}/create`, response.data)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async update ( pk:string|number, data:object ) {
        try {
            const response:{data:object} = await axios.put(`${this.url}${pk}/`, data=data, this.config)
            store.commit(`${this.storeName}/update`, response.data)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async archive ( pk:number ) {
        try {
            const data = {
                date_archived: new Date()
            }
            await axios.put(`${this.url}${pk}/archive/`, data, this.config)
            store.commit(`${this.storeName}/remove`, pk)
            return null
        } catch (e:any) {
            throw e
        }
    }
}

export default Service