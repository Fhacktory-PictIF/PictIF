
oldObj = null;

function selectLine(obj)
{
    var idLigne=obj.id;
    obj.className="danger";

    if (oldObj!=null)
    {
        oldObj.className = "";
        oldObj = obj;
    }
    else
    {
        oldObj = obj;
    }
}

/*
function addBlock()
{
    var objId, i, elmt;
    var contenu = new Array();
    var resultat;

    if (oldObj != null)
    {
        objId = oldObj.id;
        switch(objId)
        {
            case "ligne1":
                msg = msg + "ligne 1";
                break;
            case "ligne2":
                msg = msg + "ligne 2";
                break;
            case "ligne3":
                msg = msg + "ligne 3";
                break;
        }

        elmt = document.getElementById(objId);
        i = 0;
        while (elmt!=null)
        {
            objId = oldObj.id + i.toString();

            elmt = document.getElementById(objId);
            if (elmt!=null)
                contenu[i] = elmt.innerHTML;
            i++;
        }
    }
}
*/