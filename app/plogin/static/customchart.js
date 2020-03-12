var chart = new Gauge("chartContainer1", {
    title:{ text: "Total Projects employing this skill" },
maximum : 100,
    data : { y:25} });
chart.render();

function Gauge(containerId, gauge){

    gauge.unoccupied = {

        y: gauge.maximum - gauge.data.y , 
        color: "#DEDEDE",
    toolTipContent: null, 
    highlightEnabled: false,
    click : function (){ gauge.unoccupied.exploded = true; }
    
    };

    gauge.data.click = function (){ gauge.data.exploded = true; };

    if(!gauge.data.color)
        gauge.data.color = "#69C434";
  
    gauge.valueText = { text: gauge.data.y.toString(), verticalAlign: "center", dockInsidePlotArea: true };

var chart = new CanvasJS.Chart(containerId,{

           subtitles: [ gauge.valueText ],
    
      data:[{
        type: "doughnut",          
          dataPoints: [
              { y: gauge.maximum , color: "transparent", toolTipContent: null },
            gauge.data,
            gauge.unoccupied
          ]   
        }]
    
    });
      
if(gauge.title)
    chart.options.title = gauge.title;
  
chart.gauge = gauge;
//For updating
chart.updateGauge = function (){
      this.gauge.unoccupied.y = this.gauge.maximum - this.gauge.data.y;
      this.gauge.valueText.text = this.gauge.data.y.toString();

      this.render();
}
return chart;
}




// Second


var chart = new Gauge("chartContainer2", {

    title:{ text: "Total Employees employing this skill" },
maximum : 100,
    data : { x: {{% for i in skill %}
    {i.skill_name}
    {% for j in emp_skill %}
            {% if i.skill_id == j.skill_id %}
                {j.etotal}
            {% endif %}
        {% endfor %}
        {% endfor %}}

}});
chart.render();


function Gauge(containerId, gauge){

    gauge.unoccupied = {

        x: gauge.maximum - gauge.data.x ,
        color: "#DEDEDE", 
    toolTipContent: null, 
    highlightEnabled: false,
    click : function (){ gauge.unoccupied.exploded = true; }
    
    };

    gauge.data.click = function (){ gauge.data.exploded = true; };

    if(!gauge.data.color)
        gauge.data.color = "#69C434";
  
    gauge.valueText = { text: gauge.data.y.toString(), verticalAlign: "center", dockInsidePlotArea: true };

var chart = new CanvasJS.Chart(containerId,{

           subtitles: [ gauge.valueText ],
    
      data:[{
        type: "doughnut",          
          dataPoints: [
              { x: gauge.maximum , color: "transparent", toolTipContent: null },
            gauge.data,
            gauge.unoccupied
          ]   
        }]
    
    });
      
if(gauge.title)
    chart.options.title = gauge.title;
  
chart.gauge = gauge;
//For updating
chart.updateGauge = function (){
      this.gauge.unoccupied.x = this.gauge.maximum - this.gauge.data.x;
      this.gauge.valueText.text = this.gauge.data.x.toString();

      this.render();
}

return chart;
}


// Third

var chart = new Gauge("chartContainer3", {
    var: z = "Average Employee skill rating",
    title:{ text: "Dynamic Gauge Chart" },
maximum : 100,
    data : { z: {{% for i in skill %}
    {i.skill_name}
    {% for j in emp_avgskill %}
        {% if i.skill_id == j.skill_id %}
            {j.askill}
        {% endif %}
    {% endfor %}
    {% endfor %}}
}});
chart.render();


function Gauge(containerId, gauge){

    gauge.unoccupied = {

        z: gauge.maximum - gauge.data.z ,
        color: "#DEDEDE", 
    toolTipContent: null, 
    highlightEnabled: false,
    click : function (){ gauge.unoccupied.exploded = true; }
    
    };

    gauge.data.click = function (){ gauge.data.exploded = true; };

    if(!gauge.data.color)
        gauge.data.color = "#69C434";
  
    gauge.valueText = { text: gauge.data.y.toString(), verticalAlign: "center", dockInsidePlotArea: true };

var chart = new CanvasJS.Chart(containerId,{

           subtitles: [ gauge.valueText ],
    
      data:[{
        type: "doughnut",          
          dataPoints: [
              { z: gauge.maximum , color: "transparent", toolTipContent: null },
            gauge.data,
            gauge.unoccupied
          ]   
        }]
    
    });
      
if(gauge.title)
    chart.options.title = gauge.title;
  
chart.gauge = gauge;
//For updating
chart.updateGauge = function (){
      this.gauge.unoccupied.z = this.gauge.maximum - this.gauge.data.z;
      this.gauge.valueText.text = this.gauge.data.z.toString();

      this.render();
}

return chart;
}

//Fourth

var chart = new Gauge("chartContainer4", {
    var: y = "Average Project Present Skill Rating",
    title:{ text: "Average Project Present Skill Rating" },
maximum : 100,
    data : { y: {{% for i in skill %}
    {% for j in proj_prsent_avgskill %}
            {% if i.skill_id == j.skill_id %}
                {j.proj_prsent_avgskill}
            {% endif %}
        {% endfor %}
        {% endfor %}}

}});
chart.render();


function Gauge(containerId, gauge){

    gauge.unoccupied = {

        y: gauge.maximum - gauge.data.y , 
        color: "#DEDEDE", 
    toolTipContent: null, 
    highlightEnabled: false,
    click : function (){ gauge.unoccupied.exploded = true; }
    
    };

    gauge.data.click = function (){ gauge.data.exploded = true; };

    if(!gauge.data.color)
        gauge.data.color = "#69C434";
  
    gauge.valueText = { text: gauge.data.y.toString(), verticalAlign: "center", dockInsidePlotArea: true };

var chart = new CanvasJS.Chart(containerId,{

           subtitles: [ gauge.valueText ],
    
      data:[{
        type: "doughnut",          
          dataPoints: [
              { y: gauge.maximum , color: "transparent", toolTipContent: null },
            gauge.data,
            gauge.unoccupied
          ]   
        }]
    
    });
      
if(gauge.title)
    chart.options.title = gauge.title;
  
chart.gauge = gauge;
//For updating
chart.updateGauge = function (){
      this.gauge.unoccupied.y = this.gauge.maximum - this.gauge.data.y;
      this.gauge.valueText.text = this.gauge.data.y.toString();

      this.render();
}

return chart;
}



//fifth

var chart = new Gauge("chartContainer5", {
    var: y = "Average Project Rated Skill Rating:",
    title:{ text: "Average Project Rated Skill Rating" },
maximum : 100,
    data : { y: {{% for i in skill %}
    {i.skill_name}
    {% for j in proj_rated_avgskill %}
            {% if i.skill_id == j.skill_id %}
                {j.proj_rated_avgskill}
            {% endif %}
        {% endfor %}
        {% endfor %}}

}});
chart.render();


function Gauge(containerId, gauge){

    gauge.unoccupied = {

        y: gauge.maximum - gauge.data.y , 
        color: "#DEDEDE", 
    toolTipContent: null, 
    highlightEnabled: false,
    click : function (){ gauge.unoccupied.exploded = true; }
    
    };

    gauge.data.click = function (){ gauge.data.exploded = true; };

    if(!gauge.data.color)
        gauge.data.color = "#69C434";
  
    gauge.valueText = { text: gauge.data.y.toString(), verticalAlign: "center", dockInsidePlotArea: true };

var chart = new CanvasJS.Chart(containerId,{

           subtitles: [ gauge.valueText ],
    
      data:[{
        type: "doughnut",          
          dataPoints: [
              { y: gauge.maximum , color: "transparent", toolTipContent: null },
            gauge.data,
            gauge.unoccupied
          ]   
        }]
    
    });
      
if(gauge.title)
    chart.options.title = gauge.title;
  
chart.gauge = gauge;
//For updating
chart.updateGauge = function (){
      this.gauge.unoccupied.y = this.gauge.maximum - this.gauge.data.y;
      this.gauge.valueText.text = this.gauge.data.y.toString();

      this.render();
}

return chart;
}
