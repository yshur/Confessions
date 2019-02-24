var mongoose = require('mongoose');
var Post = require('./schema/postSchema');
var random = require('mongoose-random');

exports.getIssues = (req, res) => {
    console.log('getIssues');
	var q = Post.distinct( "issues" );

	q.exec(function(err, issues)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(issues);
		res.status(200).json(issues);
	});
};
exports.getColleges = (req, res) => {
    console.log('getColleges');
	var q = Post.distinct( "college" );

	q.exec(function(err, colleges)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(colleges);
		res.status(200).json(colleges);
	});
};

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

exports.getSumMonth = (req, res) => {
    console.log('getSumMonth');
	var q = Post.aggregate(
	   [
			{$group: { _id: {
				month: {$month: {$dateFromString: {dateString: "$time" } } },
				year: {$year: {$dateFromString: {dateString: "$time" } } }
			   }, count: {$sum: 1 }
			} },
			{$project: {_id: 0, month: "$_id.month", year: "$_id.year", count: 1 } },
			{$sort: {"year": -1, "month": -1} }
	   ]);

	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};
exports.getSumColleges = (req, res) => {
    console.log('getSumColleges');
    var q = Post.aggregate(
       [
    		{$group: { _id: "$college", count: { $sum: 1 } }},
    		{$project: { _id: 0, college: "$_id", count: 1 } },
    		{$sort: { count: -1 } }
       ]);

    q.exec(function(err, colleges)  {
    	if (err) {
    		console.log(`err: ${err}`);
    		res.status(200).json(`{ err : ${err} }`);
    	}
    	console.log(colleges);
    	res.status(200).json(colleges);
    });
};
exports.getSumIssues = (req, res) => {
    console.log('getSumIssues');
    var q = Post.aggregate(
       [
    		{$project: { _id: 0, issues: 1 } },
    		{$unwind: "$issues" },
    		{$group: { _id: "$issues", count: { $sum: 1 } }},
    		{$project: { _id: 0, issue: "$_id", count: 1 } },
    		{$sort: { count: -1 } }
       ]);

    q.exec(function(err, posts)  {
    	if (err) {
    		console.log(`err: ${err}`);
    		res.status(200).json(`{ err : ${err} }`);
    	}
    	console.log(posts);
    	res.status(200).json(posts);
    });
};

exports.getSumCollegeMonth = (req, res) => {
    console.log('getSumCollegeMonth');
    var q = Post.aggregate(
       [
         {$group: { _id: {
   				month: {$month: {$dateFromString: {dateString: "$time" } } },
   				year: {$year: {$dateFromString: {dateString: "$time" } } },
          college: "$college" }, count: {$sum: 1 }
   			} },
        {$project: {_id: 0, college: "$_id.college", month: "$_id.month", year: "$_id.year", count: 1 } },
  			{$sort: {"college": 1, "year": -1, "month": -1} }
       ]);

	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};
exports.getSumIssuesMonth = (req, res) => {
    console.log('getSumIssuesMonth');
    var q = Post.aggregate(
       [
        {$project: { _id: 0, issues: 1, time: 1 } },
        {$unwind: "$issues" },
        {$group: { _id: { issue: "$issues",
         month: {$month: {$dateFromString: {dateString: "$time" } } },
         year: {$year: {$dateFromString: {dateString: "$time" } } },
          }, count: { $sum: 1 } }},
         {$project: {_id: 0, issue: "$_id.issue", month: "$_id.month", year: "$_id.year", count: 1 } },
        {$sort: {"issue": 1, "year": -1, "month": -1} }
       ]);

	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};
exports.getSumIssuesCollege = (req, res) => {
    console.log('getSumIssuesCollege');
    var q = Post.aggregate(
       [
        {$project: { _id: 0, issues: 1, college: 1, } },
        {$unwind: "$issues" },
        {$group: { _id: { issue: "$issues", college: "$college" }, count: { $sum: 1 } }},
         {$project: {_id: 0, issue: "$_id.issue", college: "$_id.college", count: 1 } },
        {$sort: {"issue": 1, "college": 1 } }
       ]);

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
