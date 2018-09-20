/**************************************
 * Leaflet JS setup                   *
 **************************************/
Building = function(title, lat, lon){
    this.title = title;
    this.latitude = lat;
    this.longitude = lon;

    this.log = function(){
        console.log(this.title);
    }
}
var planes = [
    new Building("7C6807", -1.273308, 36.807241),
    new Building("7C6838", -1.272938, 36.807010),
    new Building("7C6CA1", -1.272949, 36.807670),
    new Building("7C6CA2", -1.272514, 36.807735),
    new Building("C81D9D", -1.271983, 36.807102),
    new Building("C82009", -1.271940, 36.807317),
    new Building("C82081", -1.272508, 36.806255),
    new Building("C820AB", -1.272546, 36.806512),
    new Building("C820B6", -1.273302, 36.806753),
];
var map = L.map('map').setView([-1.273354361415031, 36.80712819099427], 18);
mapLink =
    '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
    'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data& copy ; ' + mapLink,
        maxZoom: 18,
    }).addTo(map);

for (var i = 0; i < planes.length; i++) {
    var marker = new L.marker([planes[i].latitude, planes[i].longitude])
        .bindPopup('<a href="//google.com" target="_blank" >' + planes[i].title + '</a>')
        .addTo(map);
    marker.onClick(function (e) {
        console.log("henlo");
    });
    planes[i].log()
}