
var i = 0;

$(document).ready(function() {
        // on definit un point d'attache sur chaque conteneur
    var e0 = jsPlumb.addEndpoint("container0"),
    e1 = jsPlumb.addEndpoint("container1");
        // puis on relie les deux points d'attache
    jsPlumb.connect({ source:e0, target:e1 });

        // on rend le conteneur draggable mais seul les points d'attaches bougent, les deux divs restent a leur place
       jsPlumb.draggable($("#container1"));


        // sans passer par jsplumb, l'element est deplacable
        $('#container3').draggable();


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

function addDraggableComponent(id, type) {
    var newState = $('<div>').attr('id', 'state' + i).addClass('itemDrag');

    var title = $('<div>').addClass('title').text('State ' + i);
    var connect = $('<div>').addClass('connect');
    var receiver = $('<div>').addClass('receive');

    newState.css({
      'top': e.pageY,
      'left': e.pageX
    });

    jsPlumb.makeTarget(receiver, {
        parent: newState,
      endpoint:{
                                        anchor:[ "BottomRight", "BottomLeft"],
                                        paintStyle:endpointStyle
                                },
    });


    jsPlumb.makeSource(connect, {
      parent: newState,
      anchor: "BottomLeft"
    });

    newState.append(connect);
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
