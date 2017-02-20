//svg
d3.select("#container")
.append("svg:svg")
//width,height
.attr("width",500)//attribute
.attr("height",250)//attribute
//类jquery链式结构


//d3向svg中添加g元素
g =d3.select("svg")
.append("g")
.attr("transform","translate(50,30)");
//添加偏移值 transform

//定义数据
var data =[1,3,5,7,8,4,3,7]
var line_generator= d3.svg.line()
.x(func)//0,1,2,3...
.y()//1,3,5,...

//在g中生成图表
d3.select("g")
.append("path")
.attr('d', line_generator);
//d="M1,0L20,40L40,50L100,100L0,"d-path data


