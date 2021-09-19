export default function ({ store, redirect }) {
    if (store.state.auth.loggedIn) {
        console.log('Authenticated. Redirecting...')
        return redirect('/home')
    }
}