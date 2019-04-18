const express = require('express');
const app = express()
const port = process.env.PORT || 8081

app.get('/', (req, res) => {
  res.send('Hello world');
})

app.post('/webhook', (req, res) => {
  console.log('Received');
  console.log(req.body);
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify({'message': 'Hello eiei.'}));
})

app.listen(port, () => {
  console.log(`Start server at port ${port}`)
})