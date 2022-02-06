import React, {useEffect, useState} from 'react';
import {useParams} from "react-router-dom";
import '../PostDetail/PostDetail.css';

const PostDetail = () =>{

    const [postDetail, setPostData] = useState([]);
    const {slug} = useParams();

    useEffect(() => {

        fetch(`http://127.0.0.1:8000/api/post-detail/${slug}`)
            .then(res => res.json())
            .then(data => setPostData(data))
    }, []);

    const imageStyle = {
        height: "450px",
        objectFit: "cover",

    };

    return(
        <div>
            <section id="post-detail">
                <div className="container">
                    <h3 className="text-center">Post Details</h3>
                    <hr/>
                    <div className="row">
                        <div className="col-sm-12 col-md-9 col-lg-9 col-xl-9">
                            <div className="post-description">
                                <img src={postDetail.image} alt="" className="img-fluid"  style={imageStyle}  />
                                <h3 className="text-capitalize mt-2">{postDetail.title}</h3>
                                <h3>{postDetail.category}</h3>
                                <p>postDetail.description</p>
                            </div>
                        </div>
                        <div className="col-sm-12 col-md-3 col-lg-3 col-xl-3">
                            <div className="related-post">
                                <h4>Related Post</h4>
                                <hr/>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
};

export default  PostDetail;