
const extrabold = 'FiraSans-ExtraBold'

const bold = 'FiraSans-Bold'

const semibold = 'FiraSans-SemiBold'

const medium = 'FiraSans-Medium'

const regular = 'FiraSans-Regular'

const light = 'FiraSans-Light'

const fontSize = size => {
    if ( size == 1 ) return { fontSize: 30 }
    else if ( size == 2 ) return { fontSize: 25 }
    else if ( size == 3 ) return { fontSize: 20 }
    else if ( size == 4 ) return { fontSize: 18 }
    else if ( size == 5 ) return { fontSize: 16 }
    else return { fontSize: 14 }
}

const defaultText = {
    fontFamily: regular,
    fontSize: 14,
}

export { defaultText, extrabold, bold, semibold, medium, regular, light, fontSize }