import React from 'react'
import './comps.css'
import CanvasJSReact from '../assets/canvasjs.react'
import Map from './Map/Map';
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
export const Mos = (props) => {
    function grafica(datos){
        if(datos!=null){
            var Titulo=[]
            var Valor=[]
            var DataPoints=[]
            for(let x in datos){
                let Campos=datos[x]  
                Titulo.push(Campos[0])
                Valor.push(Campos[1])
            } 
            let labs=[]
            let val=[]
            labs = Titulo[0]
            val = Valor[0]
            for(let x in labs){
                DataPoints.push({label:labs[x],y:val[x]})
            }
            const grafico = {
                title: {
                  text: "Grafico de cantidad"
                },
                axisY: {
                    includeZero: true
                },
                axisX:{
                    labelFontSize: 10,
                    labelAutoFit: true
                  },
                data: [{				
                          type: "area",
                          dataPoints: DataPoints
                          
                 }]
             }
            return(
                <CanvasJSChart options = {grafico}/>
            )
        }
    }

    function mapear(ubicacion){
        if(ubicacion!=null){
            return (
                <Map/>
            )
        }
    }
    return(
        <div>
                <div>
                    {grafica(props.datos)}
                </div>
            <br/>
                <div id="mapContainer">
                    {mapear(props.ubicacion)}
                </div>
        </div>       
    )
}