
oldObj = null;

function checkWords(dictionary, words, table, id) {
    $.map(dictionary, function(v,k) {
        var block = v.toLowerCase();
        var remove = false;

        if(words != null) {
            $.each(words, function(key, word) {
                if(word.length != 0 && block.indexOf(word) < 0) {
                    remove = true;
                }
            });
        }

        if(!remove) {
            var tr = document.createElement('tr');
            tr.setAttribute("id", "a" + id);
            tr.setAttribute("class", "item");
            tr.setAttribute("onclick", "selectLine(this)");

            var td = document.createElement('td');
            td.innerHTML = v;

            tr.appendChild(td);
            table.appendChild(tr);
        }
        id += 1;
    });
}

Object.size = function(obj) {
    var size = 0, key;
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};

function checkSearch(data, words) {
    var table = document.getElementById('blockslist');
    table.innerHTML = "";
    var tbody = document.createElement('tbody');
    table.appendChild(tbody);
    id = 0;

    checkWords(data.io, words, tbody, id);
    id += Object.size(data.io);
    checkWords(data.processors, words, tbody, id);
    id += Object.size(data.processors);
    checkWords(data.selectors, words, tbody, id);
    id += Object.size(data.selectors);
    checkWords(data.statistics, words, tbody, id);
    id += Object.size(data.statistics);
}

function fillInitTable() {
    $.getJSON('/block/list', function(data) {
        checkSearch(data, null);
    });
}

$('#search').on('input', function() {
    $.getJSON('/block/list', function(data) {
        var words = $('#search').val().toLowerCase().split(' ');
        checkSearch(data, words);
    });
});

function notify(msg)
{
    $('#console').val($('#console').val() + msg);
}

function selectLine(obj) {
    var idLigne=obj.id;
    obj.className="danger";
    $("#addButton").removeAttr("disabled");

    if (oldObj!=null) {
        oldObj.className = "";
        oldObj = obj;
    }
    else {
        oldObj = obj;
    }
}

function addBlock() {
    if(oldObj != null) {
        var type = document.getElementById(oldObj.id).firstChild.innerHTML;

        $.ajax({
            url: '/block/add/' + type,
            type: 'POST',
            dataType: "json",
            data: JSON.stringify("data"),
            success : function(data){
                if(data.ok)
                {
                    notify(type + " block added\n");
                    addDraggableComponent(data.id, type)
                }
                else
                {
                    notify("Error: " + type + " block could not be added\n");
                }
            }});
    }
}

/*
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
*/

function execute() {
    notify("Executing node TODO...");
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
    $("#saveButton").attr("disabled", "disabled");
    notify("Saving work flow...");
    //Save everything
    $.ajax({
        url: '/save',
        type: 'POST',
        dataType: "json",
        data: JSON.stringify("data"),
        success : function(data){
            if(data.ok)
            {
                notify("Done\n");
            }
            else
            {
                notify("\nError: workflow could not be saved\n");
            }
            $("#saveButton").removeAttr("disabled");
        }});

}

$("#addButton").attr("disabled", "disabled");
fillInitTable();
