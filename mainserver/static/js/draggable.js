
var dictType = {'Camera stream Reader': [0,1], 'Picture Writer' : [1,0], 'Picture Reader' : [0,1], 'Cropper' : [1,1], 'Gray Scale': [1,1], 'Chromakey':[2,1], 'Image Bluhrer' : [1,1], 'Splitter':[1,2], 'File Filter':[1,1], 'Joiner':[2,1]}

/* Getting Handlebar templates */
readerTemplate = loadTemplate('#reader-template');

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
                    data: JSON.stringify({"currentId": params.targetId , "parentId":params.sourceId }),
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

var clearTableSelection = function() {
  $("#addButton").attr("disabled", "disabled");

    var table = document.getElementById("blockslist");
    for (var i = 0, row; row = table.rows[i]; i++) {
        row.removeAttribute("class");
    }
}

var onClickElement = function(obj){
  clearTableSelection();
  $("#executeButton").removeAttr("disabled");
  //$("#removeButton").removeAttr("disabled"); TODO remove when operational

  $.ajax({
      url: '/getDescription/' + obj.getAttribute('id'),
      type: 'GET',
      async: false,
      dataType: "json",
      contentType: 'application/json;charset=UTF-8',
      success : function(data){
        currentComponent = data;
        console.log(data);
        currentPicIdx = 0;
        $("#description").val(data.strDesc);
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
        var content;
        if (data.class == "Reader")
        {
            content = readerTemplate({"id" :obj.getAttribute('id')})
        } 
        $("#configuration").html(content);
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

        //TODO CONFIGURATION READONLY
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
    var newComponent = $('<div>').attr('id', String(id)).attr('onclick',"javascript: onClickElement(this)").addClass('itemDrag');
    var title = $('<div>').addClass('title').text(type);
    var connect = $('<div>').addClass('connect');

    newComponent.css({
      'top': 20,
      'left': 20
    });

    newComponent.append(title);
    $('#container').append(newComponent);
    jsPlumb.draggable($(".itemDrag"));

    switch(String(dictType[type]))
    {
        case String([0,1]):
            //source out Middle
            jsPlumb.addEndpoint(String(id), {anchor:"Right", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
            }});
        //fin case
            break;

        case String([0,2]):
            //source out Top
            jsPlumb.addEndpoint(String(id), {anchor:"TopRight", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
                }});

            //source out Bot
            jsPlumb.addEndpoint(String(id), {anchor:"BotRight", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
                }});
        //fin case
            break;

        case String([1,1]):
            //source out Middle
            jsPlumb.addEndpoint(String(id), {anchor:"Right", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
            }});

            //target In Left
            jsPlumb.addEndpoint(String(id),  {
                anchor:"Left",
                isTarget:true,
                beforeDrop: function(params) {

                    return dropFunction(params);
                }
            });
            break;

        case String([2,1]):
            //target In Bot
            jsPlumb.addEndpoint(String(id),  {
                anchor:"BottomLeft",
                isTarget:true,
                beforeDrop: function(params) {

                    return dropFunction(params);
                }
            });

            //target In Top
            jsPlumb.addEndpoint(String(id),  {
                anchor:"TopLeft",
                isTarget:true,
                beforeDrop: function(params) {

                    return dropFunction(params);
                }
            });

            //source out Middle
            jsPlumb.addEndpoint(String(id), {anchor:"Right", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
            }});

        //fin case
            break;

        case String([1,2]):

            //target In Left
            jsPlumb.addEndpoint(String(id),  {
                anchor:"Left",
                isTarget:true,
                beforeDrop: function(params) {

                    return dropFunction(params);
                }
            });
            //source out Top
            jsPlumb.addEndpoint(String(id), {anchor:"TopRight", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
                }});

            //source out Bot
            jsPlumb.addEndpoint(String(id), {anchor:"BotRight", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
                }});
            break;

        case String([2,2]):

            //source out Top
            jsPlumb.addEndpoint(String(id), {anchor:"TopRight", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
            }});

            //source out Bot
            jsPlumb.addEndpoint(String(id), {anchor:"BotRight", isSource:true, maxConnections:5, connectorStyle : { strokeStyle:"#666" }, endpoint:"Rectangle",
                beforeDetach: function(conn) {
                    return detachFunction(conn);
            }});
            break;

        case String([2,0]):
            //target In Bot
            jsPlumb.addEndpoint(String(id),  {
                anchor:"BottomLeft",
                isTarget:true,
                beforeDrop: function(params) {

                    return dropFunction(params);
                }
            });

            //target In Top
            jsPlumb.addEndpoint(String(id),  {
                anchor:"TopLeft",
                isTarget:true,
                beforeDrop: function(params) {

                    return dropFunction(params);
                }
            });
            break;

        case String([1,0]):

            //target In Left
            jsPlumb.addEndpoint(String(id),  {
                anchor:"Left",
                isTarget:true,
                beforeDrop: function(params) {

                    return dropFunction(params);
                }
            });

            break;

}};


var submitReader = function() {
  var path = $(".reader").find('input').val();
  var id = $(".reader").find("strong").text();
  $.ajax({
      url: '/setPathes/' + id,
      type: 'POST',
      async: false,
      dataType: "json",
      data: JSON.stringify({"pathes":  path}),
      contentType: 'application/json;charset=UTF-8',
      });
};
