var express = require('express');
var router = express.Router();

var data = require('../public/javascripts/resultModel');
var parser = require('body-parser');


/* GET home page. */
router.get('/', function(req, res, next) {
    // res.render('index', { title: 'Express' });
    console.log("receive message type: ")
    data.find({"Stknme":"京东方A", 'Trdtim':req.query.Trdtim},{'_id':0,'Stknme':1,'Trdtim':1,'Avgpri':1,'Ttlqty':1,'Ttlmon':1},function(err, doc) {
            if (err) {
                console.log(err.message);
            } else {
                if (doc.length > 0) {
                    console.log(doc);
                    res.send(doc);
                }
                else {
                    res.send('');
                }
            }
        });

});

module.exports = router;


// const code = parseInt(req.query.type)
// switch (code) {
//     case 1:
//         //以京东方A为例 每日股价
//         data.find({'Stknme':'京东方A','Trdtim':req.query.Trdtim},{'_id':0,'Avgpri':1},function(err, doc) {
//             if (err) {
//                 console.log(err.message);
//             } else {
//                 if(doc.length>0){
//                     console.log(doc);
//                     res.send(doc);
//                 }
//                 else {
//                     res.send('');
//                 }
//             }
//         });
//         break
//     case 2:
//         // 所有股票 每日股价
//         // TODO 查找某几种股票就好
//         data.find({'Trdtim':req.query.Trdtim},{'_id':0,'Stknme':1,'Trdtim':1,'Avgpri':1,'Total':1},function(err, doc) {
//             if (err) {
//                 console.log(err.message);
//             } else {
//                 if (doc.length > 0) {
//                     console.log(doc);
//                     res.send(doc);
//                 }
//                 else {
//                     res.send('');
//                 }
//             }
//         });
//         break
//     case 3:
//         //
//         data.find({'Trdtim':req.query.Trdtim},{'_id':0,'Stknme':1,'Trdtim':1,'Avgpri':1,'Total':1},function(err, doc) {
//             if (err) {
//                 console.log(err.message);
//             } else {
//                 if (doc.length > 0) {
//                     console.log(doc);
//                     res.send(doc);
//                 }
//                 else {
//                     res.send('');
//                 }
//             }
//         });
//         break
//     case 4:
//         data.find({'Trdtim':req.query.Trdtim},{'_id':0,'Stknme':1,'Trdtim':1,'Avgpri':1,'Total':1},function(err, doc) {
//             if (err) {
//                 console.log(err.message);
//             } else {
//                 if (doc.length > 0) {
//                     console.log(doc);
//                     res.send(doc);
//                 }
//                 else {
//                     res.send('');
//                 }
//             }
//         });
//         break
//
// }
