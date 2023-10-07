import { createApp } from 'vue'
import App from './App.vue'
import Vuesax from 'vuesax3'
import 'vuesax3/dist/vuesax.css'
import 'echarts';
import axios from 'axios'
import VueAxios from 'vue-axios'
import globalMixins from './mixins/globalMixins';

const app = createApp(App)
app.use(Vuesax)
app.use(VueAxios, axios)
app.mixin(globalMixins)
app.mount('#app')
