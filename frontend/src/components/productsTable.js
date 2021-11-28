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
						<th>Std Id</th>
						<th>Student Name</th>
						<th>Course Name</th>
						<th>Batch</th>
						<th>Teacher Name</th>
						<th>Fees</th>
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
                                <td>{product.std_id}</td>
                                <td>{product.std_name}</td>
                                <td>{product.course_name}</td>
                                <td>{product.batch}</td>
                                <td>{product.tch_name}</td>
                                <td>{product.fees}</td>
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
