fetch("/api/system")
    .then(reponse => reponse.json())
    .then(data => {
        console.log(data);
    });