import React, { Component } from "react";
// 001 - Importing CSS
import "./Map.css";
// 002 - Adding H declaration in Window
  interface Window {
    H: any;
  }
// 003 - Defining IProps Interface with debug prop
interface IProps {
  debug?: boolean;
}
// 004 - Defining  IState interface with all attributes we need
interface IState {
  lat: number;
  lng: number;
  zoom: number;
}

// 005 - Defining component with Typescript Generic
class Map extends Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    // 006 - Setting some Default (Colosseum - Rome)
    this.state = {
      lat: 41.890251,
      lng: 12.492373,
      zoom: 18
    };
  }

  // 007 - Implementing componentDidMount in order to load map once the component is mounted
  componentDidMount() {
    // 008 - Using H (a Class exported by HERE Map Javascript)
    let H = (window as any).H;
    // 009 - Instancing Map Platform
    var platform = new H.service.Platform({
      // 010 - Using the parameter defined in .env.local
      apikey: '2X-PzvrCk1EE7L-q0o9erxnfTfpkNgiBtXmvXqxdbRg'
    });
    // 011 - Defining default Layers to apply on map
    var defaultLayers = platform.createDefaultLayers();

    // 012 - initialize the map
    var map = new H.Map(
      document.getElementById("map"),
      defaultLayers.vector.normal.map,
      {
        // 013 - using state for lat, lng and zoom
        center: { lat: this.state.lat, lng: this.state.lng },
        zoom: this.state.zoom,
        pixelRatio: window.devicePixelRatio || 1
      }
    );
    // 014 - incline the Map
    map.getViewModel().setLookAtData({ tilt: 45, heading: 0 });
    // 015 - add a resize listener to make sure that the map occupies the whole container
    window.addEventListener("resize", () => map.getViewPort().resize());
    new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
    // 016 - Create the default UI components
    H.ui.UI.createDefault(map, defaultLayers);
  }
  render() {
    // 017 - implement render function
    return (
      <div className="mapWrapper">
        <div className="map" id="map"></div>
      </div>
    );
  }
}
export default Map;