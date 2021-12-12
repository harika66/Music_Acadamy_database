import react from 'react'
import ProductsTable from './productsTable'

const ProductsRow = ({user_id,is_student,is_teacher,name,email,phone}) => {
    return (
        <tr>
            <td>{user_id}</td>
			<td>{is_student}</td>
			<td>{is_teacher}</td>
			<td>{name}</td>
			<td>{email}</td>
			<td>{phone}</td>
            <td>
                <button className = "btn btn-outline-info btn-sm ml-1 mr-2">Delete</button>
            </td>
        </tr>
    );
}

export default ProductsRow