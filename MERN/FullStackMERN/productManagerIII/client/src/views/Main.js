import React, {useState, useEffect} from 'react'
import axios from 'axios';
import ProductForm from '../components/ProductForm';
import ProductList from '../components/ProductList';

const Main = (props) => {
    const [products, setProducts] = useState();
    const [loaded, setLoaded] = useState(false);


    useEffect (() =>{
        axios.get('http://localhost:8000/api/products')
            .then(res => {
                setProducts(res.data);
                setLoaded(true);
                console.log("this is in the main");
            })
            .catch(err => console.error(err));
    }, []);

    const removeFromDom = productId => {
        setProducts(products.filter(product => product._id !== productId));
    }

    return (
        <div>
            <ProductForm/>
            <hr/>
            <br/>
            {loaded && <ProductList products={products} removeFromDom={removeFromDom}/>}
        </div>
    )
};

export default Main;



