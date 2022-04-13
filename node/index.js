const http = require("http");
const axios = require('axios');
const baseURL = 'http://mobile.campushoytest.com'

const onResponse = (res, response) => {
    if(!res || !response) return;
    const data = res.data || {};
    const body = JSON.stringify(data);
    const heads = res.headers || {};
    Object.keys(heads).forEach(key => response.setHeader(`'${key}'`, heads[key]));
    response.writeHead(res.status, {
        'Content-Length': Buffer.byteLength(body),
        'Content-Type': heads['Content-Type'] || 'text/plain'
    }).end(body);
}

function onRequest(request, response) {
    const chunks = [];
    request.on('data', chunk => {
        chunks.push(chunk)
    });
    request.on('end', () => {
        const { url, method, headers } = request;
        console.log(`${method}, ${url}`);
        headers.host = baseURL;
        const heads = {};
        Object.keys(headers).forEach(key => heads[`'${key}'`] = headers[key]);
        const config = {
            timeout: 15000,
            url,
            method,
            baseURL,
            headers: heads,
            xsrfCookieName: '',
            xsrfHeaderName: '',
        };
        try {
            const payload = JSON.parse(chunks.join(''));
            const key = 'get' == method.toLowerCase() ? 'params' : 'data';
            config[key] = payload;
        } catch (error) {

        }
        axios.request(config).then(res => {
            onResponse(res, response);
        }).catch(err => {
            onResponse(err.response, response);
        });
    });
}
http.createServer(onRequest).listen(9000);
