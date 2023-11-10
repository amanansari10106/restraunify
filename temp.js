

function request(method,url, )


fetch(url, {
    method: 'DELETE',
    body: JSON.stringify({
        did: "asds"
    }),
    headers: {
        'Content-type': 'application/json; charset=UTF-8',
        'Authorization' : 'Bearer 9aa4c32366ff4b728a5650636483d4e946'

    }
}).then(function (response) {
    if (response.status == 200){
        
        return response.json;
    }

    else if(response.status == 401){
        
    }
    else if(response.status == 500){

    }
    
    return Promise.reject(response);
}).then(function (data) {
    if(data["sucess"]==true){
        console.log(data["data"]);
    }
    else{
        alert(data["message"]);
    }
}).catch(function (error) {

});
