import chroma from 'chroma-js'
import Service from './generic.service'

import { Theme } from '@/types'

class ThemeService extends Service {

    constructor () {
        super('themes')
    }

    setTheme (theme:Theme) {
        const root = document.documentElement

        root.style.setProperty('--main', theme.main)
        root.style.setProperty('--second', theme.second)
        root.style.setProperty('--text', theme.text)

        root.style.setProperty('--emphasis', theme.emphasis)
        for (const shade of [50, 100, 300, 500, 700, 900]) {
            root.style.setProperty(`--emphasis-opacity-${shade.toString()}`, chroma(theme.emphasis).alpha(shade/1000).hex())
        }
        
        root.style.setProperty('--alert', theme.alert)
        root.style.setProperty('--danger', theme.danger)

        for (const [index, shade] of [100, 300, 500, 700, 900].entries()) {
            root.style.setProperty(`--scale-text-${shade.toString()}`, theme.scale_text[index])
            root.style.setProperty(`--scale-secondary-${shade.toString()}`, theme.scale_secondary[index])
        }
    }

}

export default new ThemeService()