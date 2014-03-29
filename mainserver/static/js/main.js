
oldObj = null;

$('#search').on('input', function() {
    $.getJSON('/block/list', function(data) {
        var components = data.components
        var words = $('#search').val().toLowerCase().split(' ');
        var table = document.createElement('blockslist');
        table.innerHTML = "";

        $.map(data, function(value,key) {
            $.map(data, function(value,key) {
                $row = $(this)
                var block = $row.find("td").html().toLowerCase();
                var remove = false;

                $.each(words, function(key, word) {
                    if(word.length == 0 && block.indexOf(word) < 0) {
                        remove = true;
                    }
                });

                if(!remove) {
                    var tr = document.createElement('tr');
                    line.setAttribute("id", value);
                    line.setAttribute("class", "item");
                    line.setAttribute("onclick", "selectLine(this)");

                    var td = document.createElement('td');
                    td.innerHTML = value;

                    tr.appendChild(td);
                }
            });
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
