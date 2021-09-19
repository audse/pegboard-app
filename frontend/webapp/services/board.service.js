import axios from 'axios'
import url from './service'

const boardUrl = `${url}/boards`

const BoardService = {
    
    getById: async boardId => {
        return new Promise( resolve => {
            axios.get(`${boardUrl}/${boardId}`).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    addBoard: async data => {
        return new Promise( resolve => {
            axios.post(`${boardUrl}/`, data).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    updateBoard: async (boardId, data) => {
        return new Promise( resolve => {
            axios.put(`${boardUrl}/${boardId}`, data).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    }

}

export default BoardService