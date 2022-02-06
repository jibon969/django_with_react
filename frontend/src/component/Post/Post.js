import React, {useEffect, useState} from 'react';
import { Link } from "react-router-dom";

const Post = ()=> {
    const style = {
        height: '200px',
        width: 'auto'
    };

    const [post, setPostData] = useState([]);
    useEffect(() => {

        fetch('http://127.0.0.1:8000/api/post-list/')
            .then(res => res.json())
            .then(data => setPostData(data))
    }, []);

    return(
        <div>
            <div className="container mt-2">
                <h3 className="text-center">Recent Post</h3>
                <hr/>
                <div className="row">
                    {post.map((post) => (
                        <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 col-lg-4 mb-4">
                            <div className="card">
                                <Link to={`post-detail/${post.slug}`}>
                                    <img style={style} className="card-img-top img-fluid" src={post.image} alt=""/>
                                </Link>
                                <div className="card-body">
                                    <h4 className="text-capitalize">{post.title}</h4>
                                    <p>{post.short_description}</p>
                                    <Link to={`post-detail/${post.slug}`} className="btn btn-primary btn-block">More Detail</Link>
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