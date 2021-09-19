import { LocalScheme } from '~auth/runtime'

export default class AuthScheme extends LocalScheme {
  // Override `fetchUser` method of `local` scheme
  async fetchUser (endpoint) {

    // Try to fetch user and then set
    return this.$auth.requestWith(
        this.name,
        endpoint,
        this.options.endpoints.user
    ).then((response) => {
      const user = getProp(response.data, this.options.user.property)
      this.$auth.setUser(user)

      return response
    }).catch((error) => {
      this.$auth.callOnError(error, { method: 'fetchUser' })
    })
  }
}