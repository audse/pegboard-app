import React from 'react'

import {
    SafeAreaView,
    View,
    Text,
} from 'react-native'

import Sheet from './components/elements/sheet.element'
import Heading from './components/elements/heading.element'
import { CardService } from './services'
import CardSheet from './components/sheets/card.sheet'

let card = {
    name: null,
    content: null,
}

CardService.getById('1').then( result => {
    card = Object.assign({}, result)
}).catch( e => { throw e })

const App = () => {


    return (
        <SafeAreaView style={ {flex: 1, flexDirection: 'column'} }>
            <View style={ {flex: 1, flexDirection: 'column'} }>
                <CardSheet card={card} />
            </View>
        </SafeAreaView>
    )
}

export default App
