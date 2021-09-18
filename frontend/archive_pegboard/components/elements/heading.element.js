
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

class Heading extends React.Component {

    constructor ( props ) {
        super(props)

        this.state = {

            headingStyle: Object.assign( {}, styles.heading, fontSize(props.size ? props.size : 6) ),

            overlineStyle: Object.assign( {}, styles.overline, fontSize(props.size ? props.size : 6) * 0.6 ),

            subheadingStyle: Object.assign( {}, styles.subheading, fontSize(props.size ? props.size : 6) * 0.6 ),
        }
    }

    render () {
        return (
            <View>

                { this.props.overline && this.props.overline.length > 0 &&
                    <TextBlock style={[ this.state.overlineStyle, this.props.overlineStyle ]}>
                        { this.props.overline }
                    </TextBlock>
                }

                { this.props.heading && this.props.heading.length > 0 && 
                    <TextBlock style={[ this.state.headingStyle, this.props.headingStyle ]}>
                        { this.props.heading }
                    </TextBlock>
                }

                { this.props.subheading && this.props.subheading.length > 0 && 
                    <TextBlock style={[ this.state.subheadingStyle, this.props.subheadingStyle ]}>
                        { this.props.subheading }
                    </TextBlock>
                }
            </View>
        )
    }
}

export default Heading