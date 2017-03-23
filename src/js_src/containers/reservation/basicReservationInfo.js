import React, { Component } from 'react';

class BasicReservationInfo extends Component {
  render() {
    return (
      <form>
        <div>
          <label>
            Proposed Gene Name
            <input type='text' placeholder='ABC123' />
          </label>
        </div>
        <div>
          <label>
            ORF Name
            <input type='text' />
          </label>
        </div>
        <div>
          <label>
            Description of gene name acronym
            <input type='text' />
          </label>
        </div>
         <div>
          <label>
            Notes about the gene
            <input type='text' />
          </label>
        </div>
        <div className='text-right'>
          <a className='button disabled'>Next <i className='fa fa-chevron-right' /></a>
        </div>
      </form>
    );
  }
}

export default BasicReservationInfo;
