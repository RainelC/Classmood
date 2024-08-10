let video = document.getElementById('video');
let canvas = document.getElementById('canvas');
let test = document.getElementById('test');
let ctx = canvas.getContext('2d');
let tamaño = 400;

window.onload = mostrarCamara;

function mostrarCamara() {
    let opciones = {
        audio: false,
        video: {
            width: tamaño, height: tamaño
        }
    }

    if (navigator.mediaDevices.getUserMedia){
        navigator.mediaDevices.getUserMedia(opciones)
            .then(function(stream){
                currentStream = stream;
                video.srcObject = currentStream;
                procesarCamara();
                setTimeout(attendance_do, 5000)
                // setTimeout(new_student, 5000)
            })
            .catch(function(err){
                alert("No he podido utilizar la camara :(")
            })
    }
    else{
        alert("No funco :(")
    }
}


function procesarCamara(){
    ctx.drawImage(video, 0, 0, tamaño, tamaño, 0, 0, tamaño, tamaño);
    setTimeout(procesarCamara, 20);
}



function new_student(){
    var img_data = ctx.getImageData(10, 10, tamaño,tamaño)
    var ctx2 = test.getContext('2d');
    ctx2.putImageData(img_data,0,0);
    datos = {
        "student_id": "studen_03",
        "name": "Pedro",
        "lastname": "Ramírez",
        "img": test.toDataURL()
    }
    fetch('http://127.0.0.1:8000/student/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    }).then(response => response.json())
    .then(data => console.log(data))
}

function attendance_do(){
    var img_data = ctx.getImageData(10, 10, tamaño,tamaño)
    var ctx2 = test.getContext('2d');
    ctx2.putImageData(img_data,0,0);
    datos = {
        "teacher_id": "66b6ddb9efd7d8141f592441",
        "img": test.toDataURL()
    }
    fetch('http://127.0.0.1:8000/attendance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    }).then(response => response.json())
    .then(data => console.log(data))
}






