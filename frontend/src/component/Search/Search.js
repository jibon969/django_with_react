import React, {useState, useEffect} from 'react';

const Search = () =>{
    const[data, setData] = useState([]);
    const[input, setInput] = useState('');
    const[output, setOutput] = useState([]);

    useEffect(()=>{
        fetch(`http://127.0.0.1:8000/api/post-list/`)
            .then(res=>res.json())
            .then(data=> setData(data))
    }, []);

    useEffect(()=>{
        setOutput([]);
        data.filter(val=>{
            if(val.title.toLowerCase().includes(input.toLowerCase())){
                setOutput(output=>[...output, val])
            }
        })
    });

    return(
        <div>
            <div className="container my-3">
                <div className="row justify-content-center">
                    <div className="col-sm-12 col-md-8 col-lg-8 col-xl-8 mb-4">
                        <h3 className="text-center">Search Here</h3>
                        <hr/>
                        <input onChange={e=>setInput(e.target.value)} type="text" className="form-control" placeholder="Search Here"/>
                    </div>
                </div>
                <br/>
                <div className="row">
                    {
                        output.map(item=>(
                            <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 mb-4">
                                <h3 className="text-capitalize">{item.title}</h3>
                                <p>{item.description}</p>
                            </div>
                        ))
                    }
                </div>
            </div>
        </div>
    )
};

export default Search;