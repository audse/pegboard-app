
import React from 'react';
import { View, Text } from 'react-native';

import { defaultText } from './../../styles/text.styles'

const defaultStyle = { 
    ...defaultText, 
    color: '#fefefe',
}

const TextBlock = ( { style, children } ) => {

    return (
        <Text style={ [ defaultStyle, style ] }>
            { children }
        </Text>
    )

}

export default TextBlock