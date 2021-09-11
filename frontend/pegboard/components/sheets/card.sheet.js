
import React from 'react'
import { View, Text } from 'react-native'

import Sheet from './../elements/sheet.element'
import Heading from '../elements/heading.element'
import TextBlock from '../elements/textblock.element'

const CardSheet = ( { name, content } ) => {
    <Sheet
        header={
            <Heading size={3} heading={name} />
        }

        content={
            <TextBlock>{content}</TextBlock>
        }
    />
}