import React, {useEffect, useState} from 'react';
import {useParams} from "react-router-dom"

const PostDetail = () =>{
    const [postDetail, setPostData] = useState([]);
    const {id} = useParams();
    useEffect(() => {

        fetch(`http://127.0.0.1:8000/api/post-detail/${id}`)
            .then(res => res.json())
            .then(data => setPostData(data))
    }, []);
    return(
        <div>
            <h2>{postDetail.id}</h2>
            <h2>{postDetail.title}</h2>
            <h2>{postDetail.description}</h2>
        </div>
    )
};

export default  PostDetail;