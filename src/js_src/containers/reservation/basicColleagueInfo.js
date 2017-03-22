import React, { Component } from 'react';

class BasicCollegueInfo extends Component {
  render() {
    return (
      <form>
        <div>
          <label>
            Your name
            <input type='text' />
          </label>
        </div>
        <div>
          <a>Didn't find your name?  Become an SGD colleague</a>
        </div>
        <div className='text-right'>
          <a className='button disabled'>Next <i className='fa fa-chevron-right' /></a>
        </div>
      </form>
    );
  }
}

export default BasicCollegueInfo;
