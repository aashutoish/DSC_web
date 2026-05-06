// Allow importing CSS and image assets in TypeScript files
declare module '*.css'
declare module '*.scss'
declare module '*.sass'
declare module '*.png'
declare module '*.jpg'
declare module '*.jpeg'
declare module '*.gif'
declare module '*.svg'

// Explicitly allow the side-effect import used in `_app.tsx`
declare module '../styles/globals.css'

export {}
