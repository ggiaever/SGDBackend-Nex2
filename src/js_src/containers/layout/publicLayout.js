import React, { Component } from 'react';

import style from './style.css';
import ErrorContainer from './errorContainer';

class PublicLayout extends Component {
  render() {
    return (
      <div>
        <ErrorContainer />
        <div className={`${style.publicContainer} callout row`}>
          <div className='columns small-12'>
            {this.props.children}
          </div>
        </div>
      </div>
    );
  }
}

PublicLayout.propTypes = {
  children: React.PropTypes.node,
};

export default PublicLayout;
