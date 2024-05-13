const WEATHERAPI = "e6ed093031474d538f6101732240905";

location_input = document.getElementById("id_address")
document.getElementById("locationBtn").addEventListener("click", (event) => {
    event.preventDefault();
    getLocation();
});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        location_input.value = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    api(position.coords.latitude, position.coords.longitude)
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            location_input.value = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            location_input.value = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            location_input.value = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            location_input.value = "An unknown error occurred.";
            break;
    }
}

function api(lat, long) {
    fetch(`http://api.weatherapi.com/v1/current.json?key=e6ed093031474d538f6101732240905&q=${lat},${long}&aqi=no`)
        .then(res => res.json())
        .then(data => {
            location_input.value = `${data.location.name} ${data.location.region} ${data.location.country}`
        })
}
