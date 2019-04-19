const express = require('express');
const bodyParser = require('body-parser');
const mathLib = require('mathjs');
const rp = require('request-promise');
const app = express()
const port = process.env.PORT || 8081

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json({ type: 'application/*+json' }));
app.use(bodyParser.json());
app.use(express.static('public'));

const weatherConfig = {
  appID: "25370c1dcd88f560ee7021ead58a657c"
}

app.get('/', (req, res) => {
  res.send('Hello world');
})

app.post('/webhook', async (req, res) => {
  res.setHeader('Content-Type', 'application/json');

  let output;

  if (req.body.queryResult.intent.displayName == "Calculator") {
    output = { 'fulfillmentText': mathLib.eval(req.body.queryResult.parameters.expression) }
  } else if (req.body.queryResult.intent.displayName == "Time Telling") {
    output = { 'fulfillmentText': 'ขณะนี้เวลา ' + new Date(Date.now()).toLocaleString('en-GB', { timeZone: "Asia/Bangkok" }) }
  } else if (req.body.queryResult.intent.displayName == "Weather") {
    let weatherResult = await rp({
      uri: `https://api.openweathermap.org/data/2.5/weather?q=${req.body.queryResult.parameters['geo-city']}&APPID=${weatherConfig.appID}`,
      json: true
    });
    //console.log(weatherResult);
    let temp = weatherResult.main.temp;
    output = { 'fulfillmentText': "ตอนนี้อุณหภูมิ " + (temp - 272.15) + ' องศา' };
  } else {
    output = { 'fulfillmentText': "What are you talking about?" }
  }

  await res.send(output);
})

app.listen(port, () => {
  console.log(`Start server at port ${port}`)
})