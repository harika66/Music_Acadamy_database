import react, {useContext} from "react"
import {Navbar, Nav, Form, FormControl, Button, Badge} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import { ProductContext } from "../ProductContext"
import ProductsTable from "./productsTable"

const NavBar = () =>{
const [products, setProducts] = useContext(ProductContext)

    return (
        <Navbar bg="dark" expand="lg" variant="dark">
            <Navbar.Brand href="#home">Shrine of Music</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Form inline>
                        { <Link to="/addproducts" className="btn btn-primary btn-sm mr-4">Add Student</Link>}
                        { <Link to="/students" className="btn btn-primary btn-sm mr-4">Get Students</Link> }
                        {/* <button onClick={() => ProductsTable()}  className = "btn btn-primary btn-sm mr-4">Get Students</button> */}
                </Form>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default NavBar;