const express = require('express');
const app = express()
const port = process.env.PORT || 8081

app.get('/', (req, res) => {
  res.send('Hello world');
})

app.post('/hello', (req, res) => {
  res.send('Hello eiei.');
})

app.listen(port, () => {
  console.log(`Start server at port ${port}`)
})