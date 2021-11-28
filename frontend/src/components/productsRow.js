import react from 'react'
import ProductsTable from './productsTable'

const ProductsRow = ({std_id,std_name,course_name,batch,tch_name,fees}) => {
    return (
        <tr>
            <td>{std_id}</td>
			<td>{std_name}</td>
			<td>{course_name}</td>
			<td>{batch}</td>
			<td>{tch_name}</td>
			<td>{fees}</td>
            <td>
                <button className = "btn btn-outline-info btn-sm ml-1 mr-2">Delete</button>
            </td>
        </tr>
    );
}

export default ProductsRow