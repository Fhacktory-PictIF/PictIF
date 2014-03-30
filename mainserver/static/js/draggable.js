

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

var dropFunction = function(params){
    var result = confirm("Connect " + params.sourceId + " to " + params.targetId + "?");
    if ( result == true ) {
                $.ajax({
                    url: '/block/addConnection',
                    type: 'POST',
                    async: true,
                    dataType: "json",
                    data: JSON.stringify({"currentId":  params.targetId , "parentId":params.sourceId }),
                    contentType: 'application/json;charset=UTF-8',
                    success : function(data){
                        //TODO Recuperer les donnees et ajouter un bloc au canevas
                    }});
            }
}

var addDraggableComponent = function(id, type){
    var newState = $('<div>').attr('id', String(id)).addClass('itemDrag');
    var title = $('<div>').addClass('title').text(type);
    var connect = $('<div>').addClass('connect');

    newState.css({
      'top': 20,
      'left': 20
    });

    newState.append(title);
    $('#container').append(newState);
    jsPlumb.draggable($(".itemDrag"));

    jsPlumb.addEndpoint(String(id), {anchor:"Right", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
        beforeDetach: function(conn) {
            return detachFunction(conn);
        }});
    jsPlumb.addEndpoint(String(id),  {
        anchor:"BottomLeft",
        isTarget:true,
        beforeDrop: function(params) {
             dropFunction(params);
            
        }
    });

    jsPlumb.addEndpoint(String(id),  {anchor:"TopLeft",isTarget:true});

};