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

const App = () => {

    const card = CardService.getById(1)

    return (
        <SafeAreaView style={ {flex: 1, flexDirection: 'column'} }>
            <View style={ {flex: 1, flexDirection: 'column'} }>
                <CardSheet name={card.name} content={card.content} />

            </View>
        </SafeAreaView>
    )
}

export default App;
