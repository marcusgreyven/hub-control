fetch("/api/system")
    .then(reponse => reponse.json())
    .then(data => {
        document.getElemenrById("hostname").textContent = 
            "Hostname: " + data.hostname;

        document.getElemenrById("temperature").textContent = 
            "Temperature: " + data.temperature;
    });