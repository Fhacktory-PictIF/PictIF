
oldObj = null;

$('#search').on('input', function() {
    $.getJSON('/block/list', function(data) {
        //TODO: retrieve blocks name
        });

    var words = $('#search').val().toLowerCase().split(' ');

    $("tr.item").each(function() {
        $row = $(this)
        var block = $row.find("td").html().toLowerCase();

        $.each(words, function(key, word) {
            if(word.length > 0 && block.indexOf(word) < 0) {
                $("#".concat($row.attr('id'))).remove();
            }
        });
    });
});

function notify(msg)
{
    $('#console').val($('#console').val() + msg);
}

function selectLine(obj) {
    var idLigne=obj.id;
    obj.className="danger";

    if (oldObj!=null) {
        oldObj.className = "";
        oldObj = obj;
    }
    else {
        oldObj = obj;
    }
}

function addBlock() {
    var objId;

    if(objId != null) {
        $.ajax({
            url: '/block/add/' + oldObj.id,
            type: 'POST',
            dataType: "json",
            data: JSON.stringify("data"),
            success : function(data){
                //TODO Recuperer les donnees et ajouter un bloc au canevas
            }});
        notify("Block TODO added\n");
    }
}


function reset() {
    //TODO reset un bloc selectionne sur le canevas
    $.ajax({
        url: "/block/reset/" + "TODOOOOO",
        type: 'POST',
        dataType: "json",
        data: JSON.stringify("data"),
        success : function(data){

        }});
    notify("Node reset: TODO ID\n");
}

function execute() {
    notify("Executing node TODO...");
    //TODO execute un bloc selectionne sur le canevas
    $.ajax({
        url: '/block/execute/' + 'TODOOOOO',
        type: 'POST',
        dataType: "json",
        data: JSON.stringify("data"),
        success : function(data){

        }});
    notify("Done\n");
}

function save() {
    notify("Saving work flow...");
    //Save everything
    $.ajax({
        url: '/save',
        type: 'POST',
        dataType: "json",
        data: JSON.stringify("data"),
        success : function(data){

        }});

    notify("Done\n");
}
