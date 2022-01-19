import React, {useEffect, useState} from 'react';
import { Link } from "react-router-dom";
import image from '../../static/images/blog/post1.png'

const Post = ()=>{

    var style = {
        height: '200px',
        width: 'auto'
    };


    const [post, setPostData] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/post-list/')
            .then(res => res.json())
            .then(data => setPostData(data))
    }, []);

    // Data will show only console log
    // fetch('http://127.0.0.1:8000/api/post-list/')
    //     .then(response => response.json())
    //     .then(json => console.log(json));

    return(
        <div>
            <div className="container mt-2">
                <h3 className="text-center">Recent Post</h3>
                <hr/>
                <div className="row">
                    {post.map((post) => (
                        <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 col-lg-4 mb-4">
                            <div className="card">
                                <img style={style} className="card-img-top" src={post.image} alt=""/>
                                <div className="card-body">
                                    <h3 className="">{post.title}</h3>
                                    <p>{post.description}</p>
                                    <Link to="" className="btn btn-primary btn-block">More Detail</Link>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
};

export default Post;