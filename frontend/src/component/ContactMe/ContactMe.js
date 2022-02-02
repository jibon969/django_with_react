import React from 'react';
import { useForm } from 'react-hook-form';
import '../ContactMe/ContactMe.css';

const ContactMe =  () =>{
    const {handleSubmit, formState: { errors },} = useForm();
    const onSubmit = (data) => console.log(data);

    return(
        <div>
            <section id="contact-us">
                <div className="container">
                    <h3 className="text-center">Contact Me</h3>
                    <hr/>
                    <div className="row justify-content-center">
                        <div className="col-md-8">
                            <form onSubmit={handleSubmit(onSubmit)}>
                                <input type="text" name="first_name" className="form-control mb-3" placeholder="First Name" />
                                <input type="text" name="email" className="form-control mb-3" placeholder="E-mail Address"  />
                                <textarea name="message" className="form-control mb-2" cols="20" rows="10"></textarea>
                                <button className="btn btn-primary btn-block">Submit</button>
                            </form>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
};

export default ContactMe;