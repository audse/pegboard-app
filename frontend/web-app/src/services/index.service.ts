import axios from 'axios'

class Service {
    
    url:string = 'http://localhost:8000/api/'

    constructor ( url:string ) {
        this.url = `${this.url}${url}/`
    }

    async list () {
        try {
            return await axios.get(this.url)
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