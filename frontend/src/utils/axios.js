import axios from 'axios';

const userInstance = axios.create({
    baseURL: 'http://localhost:8000/user/',
    timeout: 5000, // timeout after 5 seconds
    headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
    },
});
const productInstance = axios.create({
    baseURL: 'http://localhost:8000/product/products',
    timeout: 50000,
    headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
    }
})

export default userInstance; productInstance;
