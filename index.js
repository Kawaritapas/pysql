var express=require("express");
var app=express();
var mysql=require("mysql"); 
app.set("view engine","ejs");
var connection=mysql.createConnection({
host: "localhost",
user: "root",
password: ,   
database: 
});
connection.connect()

app.get("/",function(req,res){
    var q="select image from testing"
    connection.query(q,function(err,results){
    if(err){
        console.log(err);
    }else{
        res.render("main",{image:results})
    }
    })
})

app.listen(3000,function(){
    console.log("server started") 
})
