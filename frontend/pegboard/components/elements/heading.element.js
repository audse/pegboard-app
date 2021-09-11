
import React from 'react';
import { View, Text } from 'react-native';

import { bold, semibold, regular, fontSize } from './../../styles/text.styles'

import TextBlock from './textblock.element';

const styles = {

    heading: {
        color: '#fefefe',
        fontFamily: bold,
        letterSpacing: 0.25,
    },

    subheading: {
        color: '#cccccc',
        fontFamily: regular,
        marginTop: 10,
    },

    overline: {
        color: 'hotpink',
        fontFamily: semibold,
        textTransform: 'uppercase',
        letterSpacing: 0.5,
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

    return (
        <View>
            <TextBlock style={[ styles.overline, overlineFontSize ]}>
                { props.overline }
            </TextBlock>
            <TextBlock style={[ styles.heading, headingFontSize ]}>
                { props.heading }
            </TextBlock>
            <TextBlock style={[ styles.subheading, subheadingFontSize ]}>
                { props.subheading }
            </TextBlock>
        </View>
    )
}

export default Heading