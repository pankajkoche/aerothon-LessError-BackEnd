
const express= require('express');
const router = express.Router();

router.get('/', function(req, res, next) {
    res.send('hey!, You are Awesome. Now you are connected with backend. keep going');
  });
  

module.exports = router;
