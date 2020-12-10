
import React,{useState} from 'react'
import { Nav, NavItem, Button, NavbarText,ButtonDropdown,DropdownItem,DropdownToggle,DropdownMenu} from 'reactstrap';
import {ConseguirArchivo,GetNombres, PostDatos, GraficarDesdeArchivo, ObtenerDatosMapa} from './consultas';
import './comps.css';
import '@szhsin/react-menu/dist/index.css';

export const Sim = (props) => {
  const [dropdownOpen, setOpen] = useState(false);
  const toggle = () => setOpen(!dropdownOpen);

  const [Lista,setLista]=useState();
  const Lst=(ListaRes)=>{
    setLista(ListaRes)
  }
  return (
    <div id="Simplificado">
      <Nav>
      <NavItem>
          <NavbarText>Manejo BD</NavbarText>
            <div className="btn-group btn-sm">
            <ButtonDropdown isOpen={dropdownOpen} toggle={toggle}>
              <Button id="caret" color="primary" onClick={()=>GetNombres(props.res,Lst)}>Cargar lista</Button>
              <DropdownToggle split color="primary" />
              <DropdownMenu>
                <DropdownItem></DropdownItem>
                {Lista}
                <DropdownItem></DropdownItem>
              </DropdownMenu>
            </ButtonDropdown>
            <Button color="info" onClick={()=>PostDatos(props.env)}>Actualizar</Button>
            </div>
        </NavItem>
      <NavItem>
            <Button color="primary" onClick={()=>GraficarDesdeArchivo(props.setGrafico,props.env,props.camps)}>Graficar Desde Archivo</Button>
            <Button color="primary" onClick={()=>ObtenerDatosMapa(props.setUbicacion,props.env,props.camps)}>Mostrar en Mapa</Button>
        </NavItem>
      </Nav>
    </div>
  );
}
