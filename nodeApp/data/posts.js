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
	);
	
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
    console.log('getSumPostsByMonth');
	var q = Post.aggregate(
	   [
		  {
			$group : {
			   _id : { month: { $month: { $dateFromString: { dateString: "$time" } } }, 
			   day: { $dayOfMonth: { $dateFromString: { dateString: "$time" } } }, 
		  year: { $year: { $dateFromString: { dateString: "$time" } } } },
			   count: { $sum: 1 }
			}
		  }
	   ]
	);
	
	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};
