import React from 'react'
import { Text, TextInput, Button, View } from 'react-native'

import Heading from './../elements/heading.element'

import { defaultText, regular, semibold, bold } from './../../styles/text.styles'
import { renderNode } from 'react-native-elements/dist/helpers'

const styles = {

    input: {
        fontFamily: regular,
        color: '#333333',
        paddingBottom: 15,
        paddingHorizontal: 10,
        paddingTop: 25,
        borderBottomWidth: 2,
        borderBottomColor: 'lightgrey',
        marginBottom: 5,
    },

    label: {
        color: '#888888',
        position: 'absolute',
        top: 25,
        left: 10, 
    },

    placeholder: 'rgba(0, 0, 0, 0)'

}

const focusStyles = {

    input: {
        borderBottomColor: 'red'
    },

    label: {
        top: 0,
    },

    placeholder: 'rgba(0, 0, 0, 0.2)'
}

class Input extends React.Component {

    constructor ( props ) {
        super ( props )
        this.onFocus = this.onFocus.bind(this)
        this.onBlur = this.onBlur.bind(this)
        this.state = {
            inputStyle: styles.input,
            labelStyle: styles.label,
            placeholderStyle: styles.placeholder,
        }
    }

    onFocus () {
        this.setState({
            inputStyle: Object.assign( {}, styles.input, focusStyles.input ),
            labelStyle:  Object.assign( {}, styles.label, focusStyles.label ),
            placeholderStyle: focusStyles.placeholder
        })
    }

    onBlur () {
        this.setState({
            inputStyle: styles.input,
            labelStyle: styles.label,
            placeholderStyle: styles.placeholder
        })
    }


    render () {
        return (
            <View syle={ { position: 'relative' } }>
                <Heading heading={ this.props.label } size={5} style={ this.state.labelStyle } />
                <TextInput
                    value={ this.props.value }
                    style={ this.state.inputStyle }
                    placeholder={ this.props.placeholder } placeholderTextColor={ this.state.placeholderStyle }
                    onFocus={ this.onFocus } onBlur={ this.onBlur }  />
            </View>
        )
    }
    
}

export default Input