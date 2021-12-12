import react, {useEffect,useState, useContext} from 'react'
import {Table} from 'react-bootstrap'
import ProductsRow from './productsRow'
import { ProductContext, ProductProvider } from '../ProductContext'
import axios from "axios";

var data = [];

const ProductsTable = () => {
//    const [products, setProducts] = useContext(ProductContext)
    const [products, setProducts] = useState({ "data": [] })
    console.log("In ProductsTable")

    useEffect(() => {
        axios.get("http://localhost:8000/students")
        .then((response) => {
            console.log("hello world!!")
            console.log(response.data)
            setProducts(response.data)
            console.log(products)
        });
    }, []);


    //  useEffect(() => {
    //      fetch("localhost:8000/students")
    //          .then((resp) => {
    //              console.log("hello world!!")
    //              console.log(resp.json())
    //              return resp.json(); 
    //          }).then(results => {  
    //               console.log(results)
    //               setProducts({ "data": [...results.data] })

    //     })
    // }, [])

//fetch('localhost:8000/students')
//        .then(response => response.json())
//        .then(data => this.setState({ totalReactPackages: data.total }));


    console.log(products.data)
    return(
        <div>
            <Table striped bordered hover>
				<thead>
					<tr>
						<th>User Id</th>
						<th>Is Student</th>
						<th>Is Teacher</th>
						<th>Name</th>
						<th>Email</th>
						<th>Phone</th>
					</tr>
				</thead>
                <tbody>
                    {products.data.map((product) => (
                    //     <ProductsRow>
                    //     std_id = {product.std_id}
                    //     std_name = {product.std_name}
                    //     course_name = {product.course_name}
                    //     batch = {product.batch}
                    //     tch_name = {product.tch_name}
                    //     fees = {product.fees}
                    // </ProductsRow>


                            <tr>
                                <td>{product.user_id}</td>
                                <td>{product.is_teacher.toString()}</td>
                                <td>{product.is_student.toString()}</td>
                                <td>{product.name}</td>
                                <td>{product.email}</td>
                                <td>{product.phone}</td>
                                <td>
                                <button className = "btn btn-outline-info btn-sm ml-1 mr-2">Delete</button>
                                </td>
                            </tr>
                    ))}
                </tbody>
			</Table>
        </div>

    );
}

export default ProductsTable;
