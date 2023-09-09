import axios from 'axios';

const axiosConfig = axios.create();
axiosConfig.defaults.baseURL = 'https://api-rest-d4ob.onrender.com';

export default axiosConfig;
