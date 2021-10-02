import Service from './index.service'

class CommentService extends Service {

    constructor () {
        super('comments')
    }

}

export default new CommentService()