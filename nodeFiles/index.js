const express = require ('express'),
    bodyParser = require('body-parser'),
    app = express(),
    port = process.env.PORT || 3000,
    words = require('./data/words')
    require('./database');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use('/includes', express.static(`${__dirname}/public`));
app.use('/', express.static('./'));

app.use( (req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept");
    res.set("Content-Type", "application/json");
    next();
});

app.all('*', (req, res, next) => {
  console.log("runs for all HTTP verbs first");
  next();
});

// app.get('/', (req,res) => {
//     console.log(`__dirname: ${__dirname}`);
//     res.status(200).sendFile(`${__dirname}/index.html`);
// });

app.get('/getTopWords', words.getTopWords);

app.listen(port, () => {
    console.log(`listening on port ${port}`);
});