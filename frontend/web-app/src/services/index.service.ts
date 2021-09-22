import axios from 'axios'
import store from './../store/index.store'
import Cookies from 'js-cookie'

class Service {
    
    url:string = 'http://localhost:8000/api/'
    store:any = store

    authConfig = {
        headers: {
            'X-CSRFToken': Cookies.get('csrftoken'),
            'Authorization':`Token ${localStorage.getItem('token')}`,
        },
        withCredentials: true,
        // xsrfCookieName: 'csrftoken'
    }

    constructor ( url:string ) {
        this.url = `${this.url}${url}/`
    }

    async list () {
        console.log(this.authConfig)
        try {
            return await axios.get(this.url, this.authConfig)
        } catch (e:any) {
            throw e
        }
    }

    async retrieve ( pk:number ) {
        try {
            return await axios.get(`${this.url}${pk}/`)
        } catch (e:any) {
            throw e
        }
    }

    async create ( data:object ) {
        try {
            return await axios.post(this.url, { data: data })
        } catch (e:any) {
            throw e
        }
    }

    async update ( pk:number, data:object ) {
        try {
            return await axios.put(`${this.url}${pk}/`, { data: data })
        } catch (e:any) {
            throw e
        }
    }
}

export default Service