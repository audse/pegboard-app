import React, { useState } from 'react'
import { Animated, Easing, Text, TextInput, Button, View } from 'react-native'

import Heading from './../elements/heading.element'

import { defaultText, regular, semibold, bold } from './../../styles/text.styles'

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

// class Input extends React.Component {

//     constructor ( props ) {
//         super ( props )
//         this.onFocus = this.onFocus.bind(this)
//         this.onBlur = this.onBlur.bind(this)
//         this.handleChange = this.handleChange.bind(this)

//         this.state = {

//             value: props.value,

//             animLabelPosition: new Animated.Value( !props.value ? 25 : 0 ),
//             animLabelSize: new Animated.Value( !props.value ? 1 : 0.9 ),
//             animPlaceholderOpacity: new Animated.Value(0),
//             placeholderTextColor: 'rgba(0, 0, 0, 0)',

//             inputStyle: styles.input,
//             labelStyle: styles.label,
//         }

//     }

//     moveLabelUp = () => {
//         Animated.timing( this.state.animLabelPosition, {
//             toValue: 5,
//             duration: 150,
//             easing: Easing.ease,
//             useNativeDriver: false,
//         }).start()
//     }

//     moveLabelDown = () => {
//         Animated.timing( this.state.animLabelPosition, {
//             toValue: 25,
//             duration: 150,
//             easing: Easing.ease,
//             useNativeDriver: false,
//         }).start()
//     }

//     shrinkLabel = () => {
//         Animated.timing( this.state.animLabelSize, {
//             toValue: 0.9,
//             duration: 150,
//             easing: Easing.ease,
//             useNativeDriver: false,
//         }).start()
//     }

//     growLabel = () => {
//         Animated.timing( this.state.animLabelSize, {
//             toValue: 1,
//             duration: 150,
//             easing: Easing.ease,
//             useNativeDriver: false,
//         }).start()
//     }

//     onFocus () {
//         if ( !this.state.value ) {
//             console.log(this.state.value)
//             this.moveLabelUp()
//             this.shrinkLabel()
//         }

//         this.setState({
//             inputStyle: Object.assign( {}, styles.input, focusStyles.input ),
//             labelStyle:  Object.assign( {}, styles.label, focusStyles.label ),
//             placeholderTextColor: 'rgba(0, 0, 0, 0.2)',
//         })
//     }

//     onBlur () {
//         if ( !this.state.value || this.state.value.length < 1 ) {
//             this.moveLabelDown()
//             this.growLabel()
//         }

//         this.setState({
//             inputStyle: styles.input,
//             labelStyle: styles.label,
//             placeholderTextColor: 'rgba(0, 0, 0, 0)',
//         })
//     }

//     handleChange = (text) => {
//         this.setState({
//             value: text
//         })
//         console.log(this.state.value)
//     }


//     render () {
//         return (
//             <View style={ { position: 'relative', backgroundColor: this.props.filled ? '#eeeeee' : 'transparent' } }>
//                 <Animated.View style={ [ { position: 'absolute', left: 10, top: this.state.animLabelPosition, transform: [{ scale: this.state.animLabelSize }] } ] }>
//                     <Heading heading={ this.props.label } size={5} headingStyle={ [ this.state.labelStyle ] } />
//                 </Animated.View>
//                 <TextInput
//                     value={ this.state.value }
//                     onChange={ this.handleChange }
//                     style={ [ this.state.inputStyle ] }
//                     placeholder={ this.props.placeholder } placeholderTextColor={this.state.placeholderTextColor}
//                     onFocus={ this.onFocus } onBlur={ this.onBlur }
//                     onChangeText={ text => this.handleChange(text) } />
//             </View>
//         )
//     }
    
// }

const Input = props => {

    const value = props.value

    const anim = {
        labelPosition: new Animated.Value( !value ? 25 : 0 ),
        labelSize: new Animated.Value( !value ? 1 : 0.9 ),
    }
    
    const [ placeholderTextColor, setPlaceholderTextColor ] = useState('rgba(0, 0, 0, 0)')

    const moveLabelUp = () => {
        Animated.timing( anim.labelPosition, {
            toValue: 5,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    const moveLabelDown = () => {
        Animated.timing( anim.labelPosition, {
            toValue: 25,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    const shrinkLabel = () => {
        Animated.timing( anim.labelSize, {
            toValue: 0.9,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    const growLabel = () => {
        Animated.timing( anim.labelSize, {
            toValue: 1,
            duration: 150,
            easing: Easing.ease,
            useNativeDriver: false,
        }).start()
    }

    const onFocus = () => {
        if ( !value || value.length < 1 ) {
            moveLabelUp()
            shrinkLabel()
        }

        inputStyle = Object.assign( {}, styles.input, focusStyles.input )
        labelStyle = Object.assign( {}, styles.label, focusStyles.label )
        setPlaceholderTextColor('rgba(0, 0, 0, 0.2)')
    }

    const onBlur = () => {
        if ( !value || value.length < 1 ) {
            moveLabelDown()
            growLabel()
        }

        inputStyle = styles.input
        labelStyle = styles.label
        setPlaceholderTextColor('rgba(0, 0, 0, 0)')
    }

    const handleChange = (event) => {
        console.log(event)
    }

    return (
        <View style={ { position: 'relative', backgroundColor: props.filled ? '#eeeeee' : 'transparent' } }>
            <Animated.View style={ [ { position: 'absolute', left: 10, top: anim.labelPosition, transform: [{ scale: anim.labelSize }] } ] }>
                <Heading heading={ props.label } size={5} headingStyle={ [ styles.input ] } />
            </Animated.View>
            <TextInput
                value={ value }
                onChange={ handleChange }
                style={ [ styles.input ] }
                placeholder={ props.placeholder } placeholderTextColor={ placeholderTextColor }
                onFocus={ onFocus } onBlur={ onBlur }
                onChangeText={ text => handleChange(text) } />
        </View>
    )
    
}

export default Input
