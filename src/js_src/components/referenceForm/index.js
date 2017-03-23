import React, { Component } from 'react';

class ReferenceForm extends Component {
  render() {
    return (
      <div>
        <p>Please enter some information about your reference</p>
        <form>
          <div className='row'>
            <div className='columns small-4'>
              <label>
                PMID
                <input type='text' />
              </label>
            </div>
            <div className='columns small-1'>
              <label>&nbsp;</label>
              <div>or</div>
            </div>
            <div className='columns small-4'>
              <label>
                DOI
                <input type='text' />
              </label>
            </div>
            <div className='columns small-3 text-right'>
              <label>&nbsp;</label>
              <a className='button disabled'>Find Reference</a>
            </div>
          </div>
          <div>
            <span> or <a>enter information manually without PMID or DOI</a></span>
          </div>
          <div className='text-right'>
            <a className='button disabled'>Next <i className='fa fa-chevron-right' /></a>
          </div>
        </form>
      </div>
    );
  }
}

export default ReferenceForm;
