  var i = 0;


$(document).ready(function() {

    var map = {};    


  var endpointStyle = {
      isTarget:true, 
      maxConnections:5,
      endpoint:"Rectangle", 
      paintStyle:{ fillStyle:"gray" }
    };


    var dropOptions = { hoverClass:"hover", activeClass:"active" },
        exampleGreyEndpointOptions = {
        endpoint:"Rectangle",
        paintStyle:{ width:25, height:21, fillStyle:'#666' },
        isSource:true,
        connectorStyle : { strokeStyle:"#666" },
        isTarget:true
    };

  $('#container').dblclick(function(e) {
        addComponent(e);
  }); 

});

var addComponent function(e){
    var newState = $('<div>').attr('id', 'state' + i).addClass('itemDrag');
    
    var title = $('<div>').addClass('title').text('State ' + i);
    var connect = $('<div>').addClass('connect');

    newState.css({
      'top': 20,  
      'left': 20
    });


    newState.append(title);
    
    
    $('#container').append(newState);
    jsPlumb.draggable($(".itemDrag"));

    jsPlumb.addEndpoint('state'+i, {anchor:"Right", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle"});
    jsPlumb.addEndpoint('state'+i,  {
        anchor:"BottomLeft",
        isTarget:true,
        beforeDrop: function(params) {
            return confirm("Connect " + params.sourceId + " to " + params.targetId + "?");
        }}
    );

    jsPlumb.addEndpoint('state'+i,  {anchor:"TopLeft",isTarget:true});
    
    i++;    
};