var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// 定义一个Schema
var result = new Schema({
    _id:Schema.ObjectId,   // 或者 'productId':{type:String}
    Stknme:String,
    Trdtime:String,
    Avgpri:String,
    Ttlmon:String,
    Ttlqty: String
})

// 输出(导出)
module.exports = mongoose.model('result',result,'test1');
