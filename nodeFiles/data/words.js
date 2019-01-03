var mongoose = require('mongoose');
var Word = require('./schema/wordsSchema');
   
exports.getTopWords = (req, res) => {
    console.log('getTopWords');
    Word.find({total:{$gt:500}},
        (err, word) => {
            if (err) {
                console.log(`err: ${err}`);
                res.status(200).json(`{ err : ${err}`);
            }
            console.log(word);
            res.status(200).json(word);
        }
    );
};