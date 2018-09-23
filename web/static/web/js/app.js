/**************************************
* Leaflet JS setup                   *
**************************************/
Building = function(title, lat, lon, featureCollection, image){
    this.title = title;
    this.latitude = lat;
    this.longitude = lon;
    this.image = lon;
    this.featureCollection = featureCollection;
    this.image = image

    this.log = function(){
        console.log(this.title);
    }
}