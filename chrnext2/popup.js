chrome.tabs.executeScript( {
    code: "window.getSelection().toString();"
}, function(selection) {
    document.getElementById("output").innerHTML = selection[0];
    const Httprq = new XMLHttpRequest();
    const theurl = "http://localhost:7000/";
    Httprq.open("POST", theurl, true);

    Httprq.onreadystatechange = function() {
        if (Httprq.readyState == 4){
            // Alert response
            alert(Httprq.responseText);
        }
    };

    Httprq.send(selection[0]);
});