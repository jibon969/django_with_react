import React, {useEffect, useState} from 'react';

const BlogCategory =()=>{
    const [categoryData, setCategoryData] = useState([]);
    useEffect(() => {

        fetch(`http://127.0.0.1:8000/api/category/${slug}`)
            .then(res => res.json())
            .then(data => setCategoryData(data))
    }, []);

    return(
        <div>
            <div className="container">
                <div className="row">
                    {
                        categoryData.map(category=>(
                            <div className="col-sm-12 col-md-4">
                                <h3>{category.title}</h3>
                            </div>
                        ))
                    }
                </div>
            </div>
        </div>
    )
};
export default BlogCategory;
