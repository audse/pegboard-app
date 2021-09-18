import React from 'react'
import { useState } from 'react'
import { Button, Text, View } from 'react-native'

import Input from '../elements/input.element'

import { defaultText, regular, semibold, bold } from './../../styles/text.styles'


const styles = {
    button: {
        fontFamily: bold,
    }
}

const BoardAddForm = () => {

    const [ name, setName ] = useState('')
    const [ description, setDescription ] = useState('')

    return (
        <View>

            <Input label='Name' value={ name } onChange={ setName }  placeholder='Great Ideas'/>
            <Input label='Description' value={ description } onChange={ setDescription }  placeholder='A place for all my best ideas.' />

            <Button style={ styles.button } title="Add Board" />
            <Text>Form: { name }</Text>

        </View>
    )
}

export default BoardAddForm