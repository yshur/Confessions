var random = require('mongoose-random');

var mongoose        = require('mongoose'),
    postSchema      = new mongoose.Schema({
			_id: { $oid: String },
			source: String,
			college: String,
			isUniversity: Boolean,
			time: Date,
			unix_time: Date,
			content: String,
			len_char: Number,
			len_words: Number,
			likes: Number,
			shares: Number,
			comments: Number,
			sum_like: Number,
			words: [ String ],
			mean_words: [ String ],
			issues: [ String ]
		}  , {collection: 'posts'});
		
	postSchema.plugin(random, { path: 'r' }); // by default `path` is `random`. It's used internally to store a random value on each doc.
 

module.exports = mongoose.model('Post', postSchema);
