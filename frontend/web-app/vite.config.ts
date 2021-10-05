import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { ViteAliases } from 'vite-aliases'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
		ViteAliases()
    ],
    server: {
        host: '127.0.0.1',
        port: 3000
    }
})
