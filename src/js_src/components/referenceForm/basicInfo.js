import React, { Component } from 'react';
import Select from 'react-select';

import AuthorList from '../editableList/authorList';

class BasicReferenceInfo extends Component {
  render() {
    return (
      <div>
        <form>
          <div className='row'>
            <div className='columns small-12'>
              <label>
                Title *
                <input type='text' />
              </label>
            </div>
          </div>
          <div className='row'>
            <div className='columns small-4'>
              <label>
                Journal
                <input type='text' />
              </label>
            </div>
            <div className='columns small-1'>
              <label>
                Volume
                <input type='text' />
              </label>
            </div>
            <div className='columns small-1'>
              <label>
                Page(s)
                <input type='text' />
              </label>
            </div>
            <div className='columns small-2'>
              <label>
                Year
                <input type='text' />
              </label>
            </div>
            <div className='columns small-2'>
              <label>
                PMID
                <input type='text' />
              </label>
            </div>
            <div className='columns small-2'>
              <label>
                DOI
                <input type='text' />
              </label>
            </div>
          </div>
          <div>
            <label>Authors</label>
            <AuthorList />
          </div>
          <div className='row'>
            <div className='columns small-3'>
              <label>
                Publication status
              </label>
              <Select name='publication_status' options={STATUS_OPTIONS} />
            </div>
          </div>
          <div className='text-right'>
            <a className='button disabled'>Next <i className='fa fa-chevron-right' /></a>
          </div>
        </form>
      </div>
    );
  }
}

const STATUS_OPTIONS = [
  { value: 'in preparation', label: 'In preparation' },
  { value: 'in press', label: 'In press' },
  { value: 'unpublished', label: 'Unpublished' }
];

export default BasicReferenceInfo;
