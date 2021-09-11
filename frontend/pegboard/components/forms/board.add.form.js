import React from 'react'
import { Button, View } from 'react-native'

import Input from '../elements/input.element'

import { defaultText, regular, semibold, bold } from './../../styles/text.styles'


const BoardAddForm = props => {

    const styles = {
        button: {
            fontFamily: bold,
        }
    }

    return (
        <View>

            <Input label='Name' placeholder='Great Ideas' />
            <Input label='Description' placeholder='A place for all my best ideas.' />

            <Button style={ styles.button } title="Add Board" />

        </View>
    )
}

export default BoardAddForm