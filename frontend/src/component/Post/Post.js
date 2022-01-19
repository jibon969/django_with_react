import React from 'react';
import { Link } from "react-router-dom";
import image from '../../static/images/blog/post1.png'
import image3 from '../../static/images/blog/post3.jpg'
import image4 from '../../static/images/blog/post4.jpg'

const Post = ()=>{

    var style = {
        height: '200px',
        width: 'auto'
    };

    return(
        <div>
            <div className="container mt-2">
                <h3 className="text-center">Recent Post</h3>
                <hr/>
                <div className="row">
                    <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 mb-4">
                        <div className="card">
                            <img style={style} className="card-img-top" src={image} alt=""/>
                            <div className="card-body">
                                <h3 className="">title</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perferendis, veritatis?</p>
                                <Link to="" className="btn btn-primary btn-block">More Detail</Link>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 mb-4">
                        <div className="card">
                            <img style={style} className="card-img-top" src={image3} alt=""/>
                            <div className="card-body">
                                <h3 className="">title</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perferendis, veritatis?</p>
                                <Link to="" className="btn btn-primary btn-block">More Detail</Link>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 mb-4">
                        <div className="card">
                            <img style={style} className="card-img-top" src={image4} alt=""/>
                            <div className="card-body">
                                <h3 className="">title</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perferendis, veritatis?</p>
                                <Link to="" className="btn btn-primary btn-block">More Detail</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default Post;