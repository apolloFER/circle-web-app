
// Simple function to generate random numbers, needed for circle location
function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

// Function for drawing a point/dot, similar to drawing a circle
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

// FUnction for drawing a circle
// Takes the canvascontext and draws an arc with a radius, fills it with color.
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

// We have to redraw the objects on each resize of the canvas, hence the main function for drawing
function draw() {
    drawCircle(pos_x, pos_y, radius);

    // iterate all points which have been clicked since the page has loaded
    for(var i = 0; i < points.length; i++) {
        var point = points[i];
        drawPoint(point["point"]["x"], point["point"]["y"], point["inside"]);
    }
}

// Process the user click
function printMousePos(event) {
    // Compensate for scrollbar
    var click_x = event.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
    var click_y = event.clientY + document.body.scrollTop + document.documentElement.scrollTop;

    // Generate the request dict which will be JSONified
    var request = {
        "point": {"x": click_x, "y": click_y},
        "circle": {"x": pos_x, "y": pos_y, "radius": radius}
    };

    // We call an async HTTP request
    var api = new XMLHttpRequest();
    api.open("POST", "api/in_circle", true);
    api.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    api.send(JSON.stringify(request));

    // Called when the backend responds
    api.onloadend = function () {
        // Only do HTTP OK status codes
        if (this.status === 200) {
            var point = JSON.parse(this.response.toString());

            // We need all points because we may need to redraw everything
            points.push(point);

            // We don't want to call redraw (duplicates would exist) so we only draw the new point.
            drawPoint(point["point"]["x"], point["point"]["y"], point["inside"]);
        }
    };
}

// Main function for resizing the canvas. Everytime the window resizes so should the canvas.
function resizeCanvas() {
    var canvas = document.getElementById('canvas');

    var w_width = window.innerWidth;
    var w_height = window.innerHeight;

    // Math max is here to compensate for the already drawn circle, show a scrollbar rather than not having a circle
    canvas.width = Math.max(w_width, pos_x + radius + 1);
    canvas.height = Math.max(w_height, pos_y + radius + 1);

    draw();
}

var width = window.innerWidth;
var height = window.innerHeight;

// Random generating the circle position and size
var radius = randomIntFromInterval(Math.min(width, height) / 32, Math.min(width, height) / 8 + 1);
var pos_x = randomIntFromInterval(radius - 1, width - radius - 1);
var pos_y = randomIntFromInterval(radius - 1, height - radius - 1);

var points = [];

// Listeners for click and resize
document.addEventListener("click", printMousePos);
window.addEventListener('resize', resizeCanvas, false);

// Call it first time for initial resizing
resizeCanvas();


