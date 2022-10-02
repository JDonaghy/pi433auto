import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap"
import * as ConfirmDialog from 'vuejs-confirm-dialog'

import './assets/main.css'

const app = createApp(App)
app.use(VueAxios, axios) 
app.use(ConfirmDialog)
app.mount('#app')


