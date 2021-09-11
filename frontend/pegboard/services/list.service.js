import axios from 'axios'
import url from './service'

const listUrl = `${url}/lists`

const ListService = {
    
    getById: async listId => {
        return new Promise( resolve => {
            axios.get(`${listUrl}/${listId}`).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    getByBoard: async boardId => {
        return new Promise( resolve => {
            const board = BoardService.getById(boardId);
            axios.get(`${listUrl}/${boardId}/board`, { params: { board: board } }).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    addList: async data => {
        return new Promise( resolve => {
            axios.post(`${listUrl}/`, data).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    updateList: async (listId, data) => {
        return new Promise( resolve => {
            axios.put(`${listUrl}/${listId}`, data).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    }

}

export default ListService