
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

    if (oldObj!=null) {
        oldObj.className = "item";
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

fillInitTable();
