import axios, { AxiosRequestConfig } from 'axios'
import store from './../store/index.store'
import Cookies from 'js-cookie'

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
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async retrieve ( pk:string ) {
        try {
            const response:{data:object} = await axios.get(`${this.url}${pk}/`, this.config)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async create ( data:object ) {
        try {
            const response:{data:object} = await axios.post(this.url, data=data, this.config)
            return response.data
        } catch (e:any) {
            throw e
        }
    }

    async update ( pk:string, data:object ) {
        try {
            const response:{data:object} = await axios.put(`${this.url}${pk}/`, data=data, this.config)
            return response.data
        } catch (e:any) {
            throw e
        }
    }
}

export default Service