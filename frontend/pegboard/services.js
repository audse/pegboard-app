
import axios from 'axios'

const prefix = 'http://localhost:8000/'

const cardPrefix = `${prefix}/cards`

const CardService = {

    getById: cardId => {
        axios.get(`${cardPrefix}/${cardId}`).then( response => {
            return response.data
        }).catch( e => { throw e })
    },

    getByList: listId => {
        const list = ListService.getById(listId)
        axios.get(`${cardPrefix}/list/${listId}`, { params: { list: list } }).then( response => {
            return response.data
        }).catch( e => { throw e })
    },

    addCard: data => {
        axios.post(`${cardPrefix}/`, data).then( response => {
            return response.data
        }).catch( e => { throw e })
    },

    updateCard: (cardId, data) => {
        axios.put(`${cardPrefix}/${cardId}`, data).then( response => {
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
    },

    getByBoard: boardId => {
        const board = BoardService.getById(boardId)
        axios.get(`${listPrefix}/board/${boardId}`, { params: { board: board } }).then( response => {
            return response.data
        }).catch( e => { throw e })
    },

    addList: data => {
        axios.post(`${listPrefix}/`, data).then( response => {
            return response.data
        }).catch( e => { throw e })
    },

    updateList: (listId, data) => {
        axios.put(`${listPrefix}/${listId}`, data).then( response => {
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
    },

    addBoard: data => {
        axios.post(`${boardPrefix}/`, data).then( response => {
            return response.data
        }).catch( e => { throw e })
    },

    updateBoard: (boardId, data) => {
        axios.put(`${boardPrefix}/${boardId}`, data).then( response => {
            return response.data
        }).catch( e => { throw e })
    }

}

export { CardService, ListService, BoardService }