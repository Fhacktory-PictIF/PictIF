
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
        addDraggableComponent(e);
  });

});

var detachFunction = function(conn){
    var result = confirm("confirm detach ?");
            alert(JSON.stringify({'currentId':JSON.stringify(conn.targetId), 'parentId':JSON.stringify(conn.sourceId)}));
            if ( result == true ) {
                $.ajax({
                    url: '/block/removeConnection',
                    type: 'POST',
                    async: true,
                    dataType: "json",
                    data: JSON.stringify({"currentId": conn.targetId, "parentId":conn.sourceId}),
                    contentType: 'application/json;charset=UTF-8',
                    success : function(data){
                        //TODO Recuperer les donnees et ajouter un bloc au canevas
                    }});
            }
};

var addDraggableComponent = function(id, type){
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

    jsPlumb.addEndpoint('state'+i, {anchor:"Right", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
        beforeDetach: function(conn) {
            detachFunction(conn);
        }});
    jsPlumb.addEndpoint('state'+i,  {
        anchor:"BottomLeft",
        isTarget:true,
        beforeDrop: function(params) {
            return confirm("Connect " + params.sourceId + " to " + params.targetId + "?");
        }
    });

    jsPlumb.addEndpoint('state'+i,  {anchor:"TopLeft",isTarget:true});

    i++;
};