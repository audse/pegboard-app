import React from 'react'
import { useRef } from 'react'
import { Animated, Easing, Text, TextInput, Button, View } from 'react-native'

import Heading from './../elements/heading.element'

import { defaultText, regular, semibold, bold } from './../../styles/text.styles'

const AnimatedInput = Animated.createAnimatedComponent(TextInput)

const styles = {

    input: {
        fontFamily: regular,
        color: '#333333',
        paddingBottom: 15,
        paddingHorizontal: 10,
        paddingTop: 25,
        borderBottomWidth: 2,
        borderBottomColor: '#dddddd',
    },

    label: {
        color: '#888888',
        position: 'absolute',
    },

}

const focusStyles = {

    input: {
        borderBottomColor: 'red'
    },
}

class Input extends React.Component {

    constructor ( props ) {
        super ( props )
        this.onFocus = this.onFocus.bind(this)
        this.onBlur = this.onBlur.bind(this)
        this.state = {

            animLabelPosition: new Animated.Value(25),
            animLabelSize: new Animated.Value(1),
            animPlaceholderOpacity: new Animated.Value(0),
            placeholderTextColor: 'rgba(0, 0, 0, 0)',

            inputStyle: styles.input,
            labelStyle: styles.label,
        }

    }

    moveLabelUp = () => {
        Animated.timing( this.state.animLabelPosition, {
            toValue: 5,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    moveLabelDown = () => {
        Animated.timing( this.state.animLabelPosition, {
            toValue: 25,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    shrinkLabel = () => {
        Animated.timing( this.state.animLabelSize, {
            toValue: 0.9,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    growLabel = () => {
        Animated.timing( this.state.animLabelSize, {
            toValue: 1,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    onFocus () {
        this.moveLabelUp()
        this.shrinkLabel()

        this.setState({
            inputStyle: Object.assign( {}, styles.input, focusStyles.input ),
            labelStyle:  Object.assign( {}, styles.label, focusStyles.label ),
            placeholderTextColor: 'rgba(0, 0, 0, 0.2)',
        })
    }

    onBlur () {
        this.moveLabelDown()
        this.growLabel()

        this.setState({
            inputStyle: styles.input,
            labelStyle: styles.label,
            placeholderTextColor: 'rgba(0, 0, 0, 0)',
        })
    }


    render () {
        return (
            <View style={ { position: 'relative', backgroundColor: this.props.filled ? '#eeeeee' : 'transparent' } }>
                <Animated.View style={ [ { position: 'absolute', left: 10, top: this.state.animLabelPosition, transform: [{ scale: this.state.animLabelSize }] } ] }>
                    <Heading heading={ this.props.label } size={5} headingStyle={ [ this.state.labelStyle ] } />
                </Animated.View>
                <AnimatedInput
                    value={ this.props.value }
                    style={ [ this.state.inputStyle ] }
                    placeholder={ this.props.placeholder } placeholderTextColor={this.state.placeholderTextColor}
                    onFocus={ this.onFocus } onBlur={ this.onBlur }  />
            </View>
        )
    }
    
}

export default Input