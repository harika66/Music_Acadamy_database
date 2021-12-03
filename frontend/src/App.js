/*https://www.youtube.com/watch?v=xRPaa2GC1Lw&list=PLU7aW4OZeUzwYXbC_mbQJdAU7JUu81RZo&index=7*/ 
//import ReactDOM from "react-dom";
//import react from 'react'
//import {Navbar, Nav, Form, FormControl, Button, Badge} from 'react-bootstrap'
import {BrowserRouter as Router, Link , Route,Switch } from 'react-router-dom'
import NavBar from './components/navBar'
import ProductsTable from './components/productsTable'
import {ProductProvider} from './ProductContext'
import ProductsRow from "./components/productsRow";
/*import AddProducts from './components/AddProducts'*/
import axios from 'axios'

function App() {
  return (
    <div>
      <Router>
        <ProductProvider>
          <NavBar />
              <Route exact path='/students' component={ProductsTable} />  
              <Route exact path='/students' component={ProductsRow} />  
        </ProductProvider>
      </Router>
    </div>
  );
}

export default App;
