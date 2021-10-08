import Service from './generic.service'

class ThemeService extends Service {

    constructor () {
        super('themes')
    }

}

export default new ThemeService()