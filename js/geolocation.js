#!/usr/bin/env node

const myElement = document.getElementById("demo");

function getLocation() {
    try {
        navigator
            .geolocation
            .getCurrentPosition(showPosition);
    } catch (error) {
        window.alert(error)
    }
};

function showPosition(position) {
    myElement.innerHTML = "Latitude: " +
        position.coords.latitude +
        "<br>Longitude: " +
        position.coords.longitude;
}