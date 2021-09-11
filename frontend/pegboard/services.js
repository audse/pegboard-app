
import axios from 'axios'

const prefix = 'http://localhost:8000'

const cardPrefix = `${prefix}/cards`

const CardService = {

    getById: async cardId => {
        return new Promise( resolve => {
            axios.get(`${cardPrefix}/${cardId}`).then( response => {
                resolve(response.data)
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    getByList: async listId => {
        return new Promise( resolve => {
            const list = ListService.getById(listId);
            axios.get(`${cardPrefix}/list/${listId}`, { params: { list: list } }).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    addCard: async data => {
        return new Promise( resolve => {
            axios.post(`${cardPrefix}/`, data).then( response => {
                return response.data;
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    updateCard: async (cardId, data) => {
        return new Promise( resolve => {
            axios.put(`${cardPrefix}/${cardId}`, data).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    }

}

const listPrefix = `${prefix}/lists`

const ListService = {
    
    getById: listId => {
        return new Promise( resolve => {
            axios.get(`${listPrefix}/${listId}`).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    getByBoard: boardId => {
        return new Promise( resolve => {
            const board = BoardService.getById(boardId);
            axios.get(`${listPrefix}/board/${boardId}`, { params: { board: board } }).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    addList: data => {
        return new Promise( resolve => {
            axios.post(`${listPrefix}/`, data).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    updateList: (listId, data) => {
        return new Promise( resolve => {
            axios.put(`${listPrefix}/${listId}`, data).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    }

}

const boardPrefix = `${prefix}/boards`

const BoardService = {
    
    getById: boardId => {
        return new Promise( resolve => {
            axios.get(`${boardPrefix}/${boardId}`).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    addBoard: data => {
        return new Promise( resolve => {
            axios.post(`${boardPrefix}/`, data).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    },

    updateBoard: (boardId, data) => {
        return new Promise( resolve => {
            axios.put(`${boardPrefix}/${boardId}`, data).then( response => {
                return response.data
            }).catch( e => { throw e })
        }).catch( e => { throw e})
    }

}

export { CardService, ListService, BoardService }