var mongoose = require('mongoose');
var Post = require('./schema/postSchema');
var random = require('mongoose-random');

exports.getRandomPosts = (req, res) => {
    console.log('getRandomPosts');
	var q = Post.find().limit(20);
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err}`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};

exports.getSumPostsByMonth = (req, res) => {
    console.log('getSumPostsByMonth');
	var q = Post.aggregate(
	   [
		  {
			$group : {
			   _id : { month: { $month: { $dateFromString: { dateString: "$time" } } }, 
			   year: { $year: { $dateFromString: { dateString: "$time" } } } },
			   count: { $sum: 1 }
			}
		  }
	   ]
	).sort({
		"_id.year": -1,
		"_id.month": -1
	});

	
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};

exports.getSumPostsByDay = (req, res) => {
    console.log('getSumPostsByDay');
	var q = Post.aggregate(
	   [
		  {
			$group : {
			   _id : { day: { $dayOfMonth: { $dateFromString: { dateString: "$time" } } },
			   month: { $month: { $dateFromString: { dateString: "$time" } } },
				year: { $year: { $dateFromString: { dateString: "$time" } } } },
			   count: { $sum: 1 }
			}
		  }
	   ]
	).sort({
		"_id.year": -1,
		"_id.month": -1,
		"_id.day": -1
	});
	
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};

exports.getSumPostsByCollege = (req, res) => {
    console.log('getSumPostsByCollege');
	var q = Post.aggregate(
	   [
		  {
			$group : {
			   _id : { college: "$college"  },
			   count: { $sum: 1 }
			}
		  }
	   ]
	).sort({
		"count": -1
	});
	
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};

exports.getIssues = (req, res) => {
    console.log('getIssues');
	var q = Post.distinct( "issues" );
	
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};

    console.log(getSumPostsByIssue);
	var q = Post.aggregate(
	   [
		  {
			$group : {
			   _id : { isUniversity: "$issues" } ,
			   count: { $sum: -1 }
			}
		  }
	   ]
	).sort({
		"count": -1
	});
	
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};
exports.getMeanWords = (req, res) => {
    console.log('getMeanWords');
	var q = Post.distinct( "mean_words" );
	
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};


