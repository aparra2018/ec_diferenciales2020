import axios from 'axios';
import React from 'react';
import {DropdownItem} from 'reactstrap';
function IsValidJSON(str){
    try{
        JSON.parse(str)
    }
    catch(event){
        return false
    }
    return true
}

export function GetDatos(){
    let config = {
      method: 'GET',
      url: 'http://localhost:8000/DB/',
      headers: { 
        'Content-Type': 'application/json'
      }
    };
    axios(config)
        .then(function (response) {
            let Data=response.data;
            console.log(Data)
        })
        .catch(function (error) {
        console.log(error);
    });
}

export function PostDatos(Archivo){
    let data = JSON.stringify({"nombre":"Fichas Clinicas","datoT":Archivo});
    let config = {
        method: 'POST',
        url: 'http://localhost:8000/DB/',
        headers: { 
            'Content-Type': 'application/json'
        },
        data : data
    };
    axios(config)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error);
        });
}


export function ConseguirArchivo(set,ID){
    let config = {
        method: 'GET',
        url: 'http://localhost:8000/ObtieneArchivo/'+String(ID),
        headers: { 
            'Content-Type': 'application/json'
        }
    };
    axios(config)
        .then((response) => {
            let Data=response.data;
            if(IsValidJSON(Data.file)===true){
                set(Data.file)
            }
            else{
                alert("El archivo no es válido")
                set(null)
            }
        })
        .catch((error) => {
            console.log(error);
        });
}

export function GraficarDesdeArchivo(setGrafico,Archivo,Campos){
    let FullData=[Archivo,Campos]
    let config = {
        method: 'POST',
        url: 'http://localhost:8000/estadisticaDesdeArchivo/',
        headers: { 
            'Content-Type': 'application/json'
        },
        data:FullData
    };
    axios(config)
        .then((response) => {
            setGrafico(response.data)
        })
        .catch((error) => {
            console.log(error);
        });
}

export function ObtenerDatosMapa(SetUbicacion,Archivo,Campos){
    let FullData=[Archivo,Campos]
    let config = {
        method: 'POST',
        url: 'http://localhost:8000/mostrarEnMapa/',
        headers: { 
            'Content-Type': 'application/json'
        },
        data:FullData
    };
    axios(config)
        .then((response) => {
            if(response.data!==false){
                SetUbicacion(response.data)
            }
            else{
                alert("Campos incorrectos")
            }
        })
        .catch((error) => {
            console.log(error);
        });
}

export function GetNombres(set,setLista){
    let config = {
        method: 'GET',
        url: 'http://localhost:8000/ObtieneNombres/',
        headers: { 
            'Content-Type': 'application/json'
        }
    };
    axios(config)
        .then((response) => {
            var Mens=[]
            let Datos=response.data;
            for(let x in Datos){
                Mens.push(<DropdownItem onClick={()=>ConseguirArchivo(set,Datos[x][1])} key={x}>{Datos[x][0]}</DropdownItem>)
            }
            setLista(Mens)
        })
        .catch((error) => {
            console.log(error);
        });
}