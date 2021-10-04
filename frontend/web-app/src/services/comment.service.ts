import Service from './generic.service'

class CommentService extends Service {

    constructor () {
        super('comments')
    }

}

export default new CommentService()