import chroma from 'chroma-js'

const autoColor = (main:string) => {
    
    const luminance = chroma(main).luminance()

    const second = chroma(main).darken().hex()
    const text = luminance>0.5 ? chroma(main).darken(4).hex() : chroma(main).brighten(4).hex()
    const emphasis = luminance>0.5 ? chroma(main).set('hsl.h', '*-1').darken(2).hex() : chroma(main).set('hsl.h', '*-1').brighten(2).hex()
    const alert = luminance>0.5 ? chroma.mix(main, '#34c0eb', 0.6, 'lch').darken(2).hex() : chroma.mix(main, '#34c0eb', 0.6, 'lch').brighten(2).hex()
    const danger =  luminance>0.5 ? chroma.mix(main, '#eba834', 0.6, 'lch').darken(2).hex() : chroma.mix(main, '#eba834', 0.6, 'lch').brighten(2).hex()

    const scaleSecondary = autoScaleSecondary(main, second)
    const scaleText = autoScaleText(main, text)
    
    return {
        second,
        text,
        emphasis,
        alert,
        danger,
        scaleSecondary,
        scaleText
    }
}

const autoScaleSecondary = (main:string, second:string) => {
    return chroma
        .scale([main, second])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(6)
}

const autoScaleText = (main:string, text:string) => {
    return chroma
        .scale([main, text])
        .mode('lab')
        .padding(0.1)
        .correctLightness()
        .colors(6)
}

export { autoColor, autoScaleSecondary, autoScaleText }