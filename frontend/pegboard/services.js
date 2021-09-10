
import axios from 'axios'

const prefix = 'http://localhost:8000/'

const cardPrefix = `${prefix}/cards`

const CardService = {

    getById: cardId => {
        axios.get(`${cardPrefix}/${cardId}`).then( response => {
            return response.data
        }).catch( e => { throw e })
    }

}

const listPrefix = `${prefix}/lists`

const ListService = {
    
    getById: listId => {
        axios.get(`${listPrefix}/${listId}`).then( response => {
            return response.data
        }).catch( e => { throw e })
    }

}

const boardPrefix = `${prefix}/boards`

const BoardService = {
    
    getById: boardId => {
        axios.get(`${boardPrefix}/${boardId}`).then( response => {
            return response.data
        }).catch( e => { throw e })
    }

}

export { CardService, ListService, BoardService }