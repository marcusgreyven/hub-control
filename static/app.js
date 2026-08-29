fetch("/api/system")
    .then(response => response.json())
    .then(data => {
        document.getElementById("hostname").textContent =
            "Hostname: " + data.hostname;

        document.getElementById("temperature").textContent =
            "Temperature: " + data.temperature + " °C";
    });