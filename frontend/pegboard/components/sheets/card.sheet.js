
import React from 'react'
import { View, Text } from 'react-native'

import Sheet from './../elements/sheet.element'
import Heading from '../elements/heading.element'
import TextBlock from '../elements/textblock.element'
import { CardService } from '../../services'

const CardSheet = ( { card } ) => {

    return (
        <Sheet
            header={
                card.name ? <Heading size={3} heading={card.name} /> : null
            }

            content={ 
                card.content ? <TextBlock>{card.content}</TextBlock> : null
            }
        />
    )
}

export default CardSheet