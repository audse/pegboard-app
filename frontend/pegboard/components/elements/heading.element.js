
import React from 'react'
import { View, Text } from 'react-native'

import { bold, semibold, regular, fontSize } from './../../styles/text.styles'

import TextBlock from './textblock.element'

const styles = {

    heading: {
        fontFamily: bold,
        letterSpacing: 0.25,
    },

    subheading: {
        fontFamily: regular,
        marginTop: 10,
    },

    overline: {
        fontFamily: semibold,
        textTransform: 'uppercase',
        letterSpacing: 0.5,
    },

    empty: {
        position: 'absolute',
        height: 0,
        width: 0,
    }
}

const Heading = props => {

    const headingFontSize = fontSize(props.size ? props.size : 6)

    const overlineFontSize = {
        fontSize: headingFontSize.fontSize * 0.6
    }

    const subheadingFontSize = {
        fontSize: headingFontSize.fontSize * 0.8
    }

    const overline = props.overline ? 
        <TextBlock style={[ styles.overline, overlineFontSize, props.style ]}>
            { props.overline }
        </TextBlock> : <Text style={ styles.empty } />

    const heading = props.heading ? 
        <TextBlock style={[ styles.heading, headingFontSize, props.style ]}>
            { props.heading }
        </TextBlock> : <Text style={ styles.empty } />

    const subheading = props.subheading ? 
        <TextBlock style={[ styles.subheading, subheadingFontSize, props.style ]}>
            { props.subheading }
        </TextBlock> : <Text style={ styles.empty } />

    return (
        <View>
            
            { overline }
            { heading }
            { subheading }

        </View>
    )
}

export default Heading