import React from 'react'
import { SafeAreaView, View } from 'react-native'
import { SafeAreaProvider } from 'react-native-safe-area-context'

import BoardAddForm from './components/forms/board.add.form'


const App = () => {

    return (
        <SafeAreaProvider>
            <SafeAreaView style={ {flex: 1, flexDirection: 'column'} }>
                <View style={ {flex: 1, flexDirection: 'column'} }>
                    <BoardAddForm />
                </View>
            </SafeAreaView>
        </SafeAreaProvider>
    )
}

export default App
