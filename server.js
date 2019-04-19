const express = require('express');
const bodyParser = require('body-parser');
const mathLib = require('mathjs');
const app = express()
const port = process.env.PORT || 8081

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json({type: 'application/*+json'}));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Hello world');
})

app.post('/webhook', (req, res) => {
  res.setHeader('Content-Type', 'application/json');

  let output;

  if (req.body.queryResult.intent.displayName == "Calculator") {
    output = {'fulfillmentText': mathLib.eval(req.body.queryResult.parameters.expression)}
  } else if (req.body.queryResult.intent.displayName == "Time Telling") {
    output = {'fulfillmentText': 'ขณะนี้เวลา' + new Date(Date.now()).toLocaleString('en-GB', { timeZone: "Asia/Bangkok"})}
  } else {
    output = {'fulfillmentText': "What are you talking about?"}
  }
  
  res.send(output);
})

app.listen(port, () => {
  console.log(`Start server at port ${port}`)
})