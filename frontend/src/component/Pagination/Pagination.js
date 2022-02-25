import React from 'react';
import './Pagination.css';

import ReactPaginate from 'react-paginate';

const Pagination = () =>{
    const handlePageClick = (data) =>{
        console.log("Clicked . ", data.selected)
    };
    return(
        <div>

            <div className="container">
                {/* PAGINATION */}
                <div className="row justify-content-center mb-4">
                <ReactPaginate
                    previousLabel={'Previous'}
                    nextLabel={'Next'}

                    breakLabel={'...'}

                    pageCount={50}

                    marginPagesDisplayed={1}
                    pageRangeDisplayed={2}

                    page changing method
                    onPageChange={handlePageClick}

                    // css classes
                    containerClassName={'pagination justify-content-center'}
                    // class for unordered list
                    pageClassName={'page-item'}        // class for each page
                    pageLinkClassName={'page-link'}      // class for anchor tag

                    previousClassName={'page-item'}
                    previousLinkClassName={'page-link'}

                    nextClassName={'page-item'}
                    nextLinkClassName={'page-link'}

                    breakClassName={'page-item'}
                    breakLinkClassName={'page-link'}

                    activeClassName={'active'}
                />
            </div>
            </div>
        </div>
    )
};

export default Pagination;