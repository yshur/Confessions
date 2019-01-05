var mongoose        = require('mongoose'),
    wordSchema      = new mongoose.Schema({

        word: {
            type:String,
            index:1
        },
        total:{
            type: Number
        }
    }, {collection: 'words_more_than_50'});

module.exports = mongoose.model('Word', wordSchema);
