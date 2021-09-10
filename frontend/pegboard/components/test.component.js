import React from 'react';
import { View, Text } from 'react-native';

const testStyle = {
    backgroundColor: 'blue',
    padding: 20,
    borderRadius: 50,
}

const test = () => {
    return (
        <View style={testStyle}>
            <Text style={{ color: 'white' }}> This is a test.</Text>
        </View>
    )
}

export default test