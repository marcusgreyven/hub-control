fetch("/api/system")
    .then(response => response.json())
    .then(data => {
        document.getElementById("hostname").textContent =
            "Hostname: " + data.hostname;

        document.getElementById("temperature").textContent =
            "Temperature: " + data.temperature + " °C";

        document.getElementById("cpu").textContent = 
            "CPU: " + data.cpu_percent;

        document.getElementById("memory").textContent = 
            "Memory: " + data.memory_available_mb + "Mb";

        document.getElementById("disk_free").textContent = 
            "Disk free: " + data.disk_free_gb + "Gb";
    });