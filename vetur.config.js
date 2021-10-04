// vetur.config.js
/** @type {import('vls').VeturConfig} */
module.exports = {
    projects: [
      './frontend/web-app', // Shorthand for specifying only the project root location
      {
        // **required**
        // Where is your project?
        // It is relative to `vetur.config.js`.
        root: './frontend/web-app',
        // **optional** default: `'package.json'`
        // Where is `package.json` in the project?
        // We use it to determine the version of vue.
        // It is relative to root property.
        package: './package.json',
        tsconfig: './tsconfig.json',
    ]
  }