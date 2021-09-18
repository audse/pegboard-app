
import React from 'react';
import { View, Text } from 'react-native';

import TextBlock from './textblock.element';

const styles = {
    card: {
        backgroundColor: '#333333',
        borderRadius: 60,
        height: 'auto',
        margin: 5,
        minHeight: 120,
    },

    header: {

        marginHorizontal: 10,
    },

    before: {
        
    },

    content: {
        marginVertical: 15,
        marginHorizontal: 10,
    },

    footer: {
    },

    spacer: {
        height: 60,
    },

    empty: {
        height: 0,
        position: 'absolute',
    }
}

const Sheet = props => {

    let header, before, content, footer, spacerTop, spacerBottom = <Text style={ styles.empty } />

    if ( props.header ) header = <TextBlock style={ styles.header }> { props.header } </TextBlock>

    if ( props.before ) before = <TextBlock style={ styles.before }> { props.before } </TextBlock>

    if ( props.content ) content = <TextBlock style={ styles.content }> { props.content } </TextBlock>
    
    if ( props.footer ) footer = <TextBlock style={ styles.footer }> { props.footer } </TextBlock>

    if ( props.header || props.content ) spacerTop = <Text style={ styles.spacer } />
    if ( props.header || props.content || props.footer ) spacerBottom = <Text style={ styles.spacer } />

    return (

        <View style={ styles.card }>
            { spacerTop }

            { header }
            { before }
            { content }
            { footer }

            { spacerBottom }
        </View>

    )
}

export default Sheet