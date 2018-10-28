var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  console.log("index render")
  res.render('index.html');
});

module.exports = router;
