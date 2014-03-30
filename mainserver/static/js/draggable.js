

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


});

var detachFunction = function(conn){
    var resultConf = confirm("confirm detach ?");
    var result = false;
            if ( resultConf == true ) {
                $.ajax({
                    url: '/block/removeConnection',
                    type: 'POST',
                    async: false,
                    dataType: "json",
                    data: JSON.stringify({"currentId": conn.targetId, "parentId":conn.sourceId}),
                    contentType: 'application/json;charset=UTF-8',
                    success : function(data){
                        result = data.ok;
                        //TODO Recuperer les donnees et ajouter un bloc au canevas
                    }});
                return result;
            }
            else {
                return result;
            }
};

var dropFunction = function(params){
    var resultConf = confirm("Connect " + params.sourceId + " to " + params.targetId + "?");
    var result = false;
    if ( resultConf == true ) {
                $.ajax({
                    url: '/block/addConnection',
                    type: 'POST',
                    async: false,
                    dataType: "json",
                    data: JSON.stringify({"currentId":  params.targetId , "parentId":params.sourceId }),
                    contentType: 'application/json;charset=UTF-8',
                    success : function(data){
                        result = Boolean(data.ok);
                        //TODO Recuperer les donnees et ajouter un bloc au canevas
                    }});
                return result;
            }
    else {
        return result ;
    }
}

var addDraggableComponent = function(id, type){
    var newState = $('<div>').attr('id', String(id)).attr('onclick',"javascript: onClickElement()").addClass('itemDrag');
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
            return dropFunction(params);
        }
    });

    jsPlumb.addEndpoint(String(id),  {anchor:"TopLeft",isTarget:true});

};