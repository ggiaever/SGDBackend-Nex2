import React, { Component } from 'react';

import style from './style.css';
import ErrorContainer from './errorContainer';

class PublicLayout extends Component {
  render() {
    return (
      <div>
        <ErrorContainer />
        <div className={`${style.publicContainer} callout`}>
          {this.props.children}
        </div>
      </div>
    );
  }
}

PublicLayout.propTypes = {
  children: React.PropTypes.node,
};

export default PublicLayout;
