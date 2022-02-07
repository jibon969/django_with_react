import React, {useEffect, useState} from 'react';

const Blog =()=>{

    const [blogData, setBlogData] = useState([]);
    useEffect(() => {

        fetch('http://127.0.0.1:8000/api/post-list/')
            .then(res => res.json())
            .then(data => setBlogData(data))
    }, []);
    if(blogData){
        return(
            <div>
                <div className="container">
                    <h2 className="text-center">Blog Post</h2>
                    <hr/>
                    <div className="row">
                        {
                            blogData.map((blog=>(
                                <div className="col-sm-12 col-md-4 mb-3">
                                    <h2>{blog.title}</h2>
                                </div>
                            )))
                        }

                    </div>
                </div>
            </div>
        )
    }
    else{
        return(
            <div>
                <div className="container">
                    <div className="row">
                        <div className="col mb-5">
                            <h3 className="text-center">No Blog Found</h3>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

};
export default Blog;