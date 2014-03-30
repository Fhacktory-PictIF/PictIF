

$(document).ready(function() {

    var map = {};
    var currentComponent = null;
    var currentPicIdx = 0;


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
  $.ajax({
      url: '/block/removeConnection',
      type: 'POST',
      async: false,
      dataType: "json",
      data: JSON.stringify({"currentId": conn.targetId, "parentId":conn.sourceId}),
      contentType: 'application/json;charset=UTF-8',
      success : function(data){
        return data.ok;
      }});
}

var dropFunction = function(params){
  $.ajax({
      url: '/block/addConnection',
      type: 'POST',
      async: false,
      dataType: "json",
      data: JSON.stringify({"currentId":  params.targetId , "parentId":params.sourceId }),
      contentType: 'application/json;charset=UTF-8',
      success : function(data){
        return data.ok;
        //TODO Recuperer les donnees et ajouter un bloc au canevas
      }});
}

var onClickElement = function(obj){
  $.ajax({
      url: '/getDescription',
      type: 'GET',
      async: false,
      dataType: "json",
      data: JSON.stringify(obj.getAttribute('id')),
      contentType: 'application/json;charset=UTF-8',
      success : function(data){
        currentComponent = data;
        currentPicIdx = 0;
        if(data.images.length <= 1)
        {
          $("#nextButton").attr("disabled", "disabled");
          $("#previousButton").attr("disabled", "disabled");
        }
        else
        {
          $("#nextButton").removeAttr("disabled");
        }

        if(data.images.length != 0)
        {
          $("#renderPic").attr('src', data.images[0]);
        }
  }});
}

var displayStaticDescription = function(blockType){
  $.ajax({
      url: '/getStaticDescription/' + blockType,
      type: 'GET',
      async: false,
      dataType: "json",
      data: JSON.stringify(blockType),
      contentType: 'application/json;charset=UTF-8',
      success : function(data){
        $("#nextButton").attr("disabled", "disabled");
        $("#previousButton").attr("disabled", "disabled");

        $("#description").val(data.strDesc);
        $("#renderPic").attr('src', "../static/img/upload_b.png");

        //TODO add configuration (readonly mode)
        for (i=0; i<data.description.lenght; i++)
          switch (data.description[i][2])
          {
            case "int":


            case "string":


            case "":
          }
  }});
}

var next = function(){
  $("#previousButton").removeAttr("disabled");
  $("#renderPic").attr('src', data.images[currentPicIdx]);
  currentPicIdx += 1;

  if(currentPicIdx == currentComponent.images.length - 1)
  {
    $("#nextButton").attr("disabled", "disabled");
  }
}

var previous = function(){
  $("#nextButton").removeAttr("disabled");
  $("#renderPic").attr('src', data.images[currentPicIdx]);
  currentPicIdx += 1;

  if(currentPicIdx == 0)
  {
    $("#previousButton").attr("disabled", "disabled");
  }
}

var addDraggableComponent = function(id, type){
    var newState = $('<div>').attr('id', String(id)).attr('onclick',"javascript: onClickElement(this)").addClass('itemDrag');
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