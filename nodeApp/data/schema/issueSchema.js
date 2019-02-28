var random = require('mongoose-random');

var mongoose        = require('mongoose'),
    issueSchema      = new mongoose.Schema({
		}  , {collection: 'issues'});

	//issueSchema.plugin(random, { path: 'r' }); // by default `path` is `random`. It's used internally to store a random value on each doc.


module.exports = mongoose.model('Issue', issueSchema);
