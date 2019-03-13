const config = {
    apiUrl: process.env.NODE_ENV === 'production' ? 'https://listview.srvz-webapp.he-arc.ch' : 'http://localhost:8000',
}

module.exports = config
