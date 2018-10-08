

var data, txt, svg, x, y, bins, bar;
var formatCount = d3.format(",.0f");

d3.json("/load_data", function (error, json_data) {

  if(!error){
     data = json_data['users'];
     map = data.map(function(d,i){ return parseFloat(d.age); })
     map2 = data.map(function(d,i){ return i; })
     console.log("Data LOADED!")
     createVis()
     console.log(map2)
  }

  else{
    console.log("Data not loaded!!!")
  }

});

function createVis(){

    // visualize the total number of users
    // use txt variable defined above


    txt = d3.select("#total_users_text")
      .append("text");
    console.log("appeneed")

    // Part 1

    // ------ YOUR CODE GOES HERE --------
    num_stud = data.length;
    console.log(num_stud)

    // into .text attribute pass the lenghts of the data
    txt.text(num_stud)

    txt
      .style("text-anchor", "start")
      .style("font-size", "30px")
      .style("font-style", "italic")
      .attr("fill", "#888")
      .attr("y", 440)
      .attr("x", 10);

    svg = d3.select("#barChart")
        margin = {top: 0, right: 45, bottom: 45, left: 0},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        console.log("width: " + width)
        console.log("height: " + height)
        g = svg.append("g")
               .attr("transform",
                     "translate(" + margin.left + "," + margin.top + ")");

    // Part 2

    // ------ YOUR CODE GOES HERE --------

    //var test_data = [50, 100, 150, 200, 250]
    var xScale = d3.scaleBand()
   //.domain(data)
   .domain(map2)
   .range([0, width])
   .padding(0.05)

   // var xScale = d3.scaleBand()
   // .domain(data)
   // .range([0, width])
   // .padding(0.2)

    svg.selectAll("rect")
    .data(data)
    .enter()
    .append("rect")
    .attr("x", function(d,i){
      return xScale(i);
      })
    .attr("y", function(d){
      return height-d.age;
    })

    .attr("width", xScale.bandwidth)
    .attr("height", function(d){
      return d.age;
    })
    .style("fill","blue")

    // a. Create x and y scale

    // b. Create bins and histogram

    // c. Create bars (rect)

    // d. Create bar labels

    // e. Call Axes

    // f. Create Axes label

}
