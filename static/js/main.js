
function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function drawPoint(x, y, inside) {
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');

    context.beginPath();
    context.arc(x, y, 1, 0, 2 * Math.PI, false);
    context.fillStyle = inside === true ? 'green' : 'red';
    context.fill();
    context.lineWidth = 3;
    context.strokeStyle = inside === true ? 'green' : 'red';
    context.stroke();
}

function drawCircle(x, y, radius) {
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');

    context.beginPath();
    context.arc(x, y, radius, 0, 2 * Math.PI, false);
    context.fillStyle = 'azure';
    context.fill();
    context.lineWidth = 1;
    context.strokeStyle = 'black';
    context.stroke();
}

function draw() {
    drawCircle(pos_x, pos_y, radius);
    for(var i = 0; i < points.length; i++) {
        var point = points[i];
        drawPoint(point["point"]["x"], point["point"]["y"], point["inside"]);
    }
}

function printMousePos(event) {
    var click_x = event.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
    var click_y = event.clientY + document.body.scrollTop + document.documentElement.scrollTop;

    var request = {
        "point": {"x": click_x, "y": click_y},
        "circle": {"x": pos_x, "y": pos_y, "radius": radius}
    };

    var api = new XMLHttpRequest();
    api.open("POST", "api/in_circle", true);
    api.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    api.send(JSON.stringify(request));


    api.onloadend = function () {
        if (this.status === 200) {
            var point = JSON.parse(this.response.toString());
            points.push(point);

            drawPoint(point["point"]["x"], point["point"]["y"], point["inside"]);
        }
    };
}

function resizeCanvas() {
    var canvas = document.getElementById('canvas');

    var w_width = window.innerWidth;
    var w_height = window.innerHeight;

    canvas.width = Math.max(w_width, pos_x + radius + 1);
    canvas.height = Math.max(w_height, pos_y + radius + 1);

    draw();
}

var width = window.innerWidth;
var height = window.innerHeight;

var radius = randomIntFromInterval(Math.min(width, height) / 32, Math.min(width, height) / 8 + 1);

var pos_x = randomIntFromInterval(radius - 1, width - radius - 1);
var pos_y = randomIntFromInterval(radius - 1, height - radius - 1);

var points = [];

document.addEventListener("click", printMousePos);
window.addEventListener('resize', resizeCanvas, false);

resizeCanvas();


