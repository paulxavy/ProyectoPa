let endPoint = 'http://127.0.0.1:8000/upload';
// Get textarea - Dom
function getVal() {
    console.log("si va")
    const val = document.querySelector('input').value;
    let data = {data: val};
    fetch(endPoint, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res =>  res.json())
    .then(response => {
        console.log('Success:', response)
        console.log(response.value);
        let result = document.getElementById("result");
        result.value = response.value;
    })
    .catch(error => console.error(error))
    

   
}
function limpiar() {
    document.getElementById("text").value = "";
    document.getElementById("result").value = "";
}

