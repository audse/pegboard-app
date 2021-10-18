import chroma from 'chroma-js'
import Service from './generic.service'

import { Theme } from '@/types'

class ThemeService extends Service {

    constructor () {
        super('themes')
    }

    resetTheme () {

        const theme = {
            id: 0,
            name: 'default',
            url: 'default',
            order: 0,
            user: {
                id: 0,
                username: 'default',
            },
            date_created: '',
            date_updated: '',
            date_archived: null,

            main: '#282c38',
            second: '#111213',
            text: '#f3f7ff',
            emphasis: '#f855a6',
            alert: '#88a4ff',
            danger: '#d3a43f',
            scale_text: [
                '#3E4659',
                '#535f79',
                '#6a7692',
                '#8692b1',
                '#b6bfd4',
                '#d1d7e4',
            ],
            scale_secondary: [
                '#242831',
                '#242831',
                '#20232b',
                '#1d1f25',
                '#191b1f',
                '#151719',
            ],
        }

        this.setTheme(theme)

    }

    setTheme (theme:Theme) {
        console.log(theme.name)
        // const root = document.documentElement
        const root = document.getElementById('page-root')

        try {
            root?.style.setProperty('--main', theme.main)
            root?.style.setProperty('--second', theme.second)
            root?.style.setProperty('--text', theme.text)
            root?.style.setProperty('--emphasis', theme.emphasis)
            root?.style.setProperty('--alert', theme.alert)
            root?.style.setProperty('--danger', theme.danger)

            for (const [index, shade] of [50, 100, 300, 500, 700, 900].entries()) {
                const alpha = shade/1000

                root?.style.setProperty(`--main-opacity-${shade}`, chroma(theme.main).alpha(alpha).hex())
                root?.style.setProperty(`--second-opacity-${shade}`, chroma(theme.second).alpha(alpha).hex())
                root?.style.setProperty(`--text-opacity-${shade}`, chroma(theme.text).alpha(alpha).hex())
                root?.style.setProperty(`--emphasis-opacity-${shade}`, chroma(theme.emphasis).alpha(alpha).hex())
                root?.style.setProperty(`--alert-opacity-${shade}`, chroma(theme.alert).alpha(alpha).hex())
                root?.style.setProperty(`--danger-opacity-${shade}`, chroma(theme.danger).alpha(alpha).hex())

                // I'm not 100% sure that there are 6 items in the `scale_text` and `scale_secondary` arrays
                if (theme.scale_text[index] !== undefined && theme.scale_secondary[index] !== undefined) {

                    root?.style.setProperty(`--scale-text-${shade}`, theme.scale_text[index])
                    root?.style.setProperty(`--scale-secondary-${shade}`, theme.scale_secondary[index])
                    
                    for (const [subIndex, subShade] of [50, 100, 300, 500, 700, 900].entries()) {
                        const subAlpha = subShade/1000
                        root?.style.setProperty(`--scale-text-${shade}-opacity-${subShade}`, chroma(theme.scale_text[index]).alpha(subAlpha).hex())
                        root?.style.setProperty(`--scale-secondary-${shade}-opacity-${subShade}`, chroma(theme.scale_secondary[index]).alpha(subAlpha).hex())
                    }
                }
            }
        } catch (e:any) { console.log(e) }
    }

}

export default new ThemeService()