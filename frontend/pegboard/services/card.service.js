import axios from 'axios'
import url from './service'

const cardUrl = `${url}/cards`

const CardService = {

    getById: async cardId => {
        return new Promise( resolve => {
            axios.get(`${cardUrl}/${cardId}`).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    getByList: async listId => {
        return new Promise( resolve => {
            const list = ListService.getById(listId);
            axios.get(`${cardUrl}/${listId}/list`, { params: { list: list } }).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    addCard: async data => {
        return new Promise( resolve => {
            axios.post(`${cardUrl}/`, data).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    updateCard: async (cardId, data) => {
        return new Promise( resolve => {
            axios.put(`${cardUrl}/${cardId}`, data).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    }

}

export default CardService