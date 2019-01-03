var mongoose        = require('mongoose'),
    wordSchema      = new mongoose.Schema({


        word: {
            type:String,
            index:1
        },
        total:{
            type: Number
        }
    }, {collection: 'colleges_words'});


module.exports = mongoose.model('Word', wordSchema);
