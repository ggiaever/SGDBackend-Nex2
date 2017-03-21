import React, { Component } from 'react';
import { connect } from 'react-redux';

import style from './style.css';
import { clearError, clearMessage } from '../../actions/metaActions';

class ErrorContainer extends Component {
  renderError() {
    if (!this.props.error) return null;
    let handleClick = () => {
      this.props.dispatch(clearError());
    };
    return (
      <div className={`alert callout ${style.errorContainer}`}>
        <h3 className={style.closeIcon} onClick={handleClick}><i className='fa fa-close' /></h3>
        <p>
          {this.props.error}
        </p>
      </div>
    );
  }

  renderMessage() {
    if (!this.props.message) return null;
    let handleClick = () => {
      this.props.dispatch(clearMessage());
    };
    return (
      <div className={`primary callout ${style.errorContainer}`}>
        <h3 className={style.closeIcon} onClick={handleClick}><i className='fa fa-close' /></h3>
        <p dangerouslySetInnerHTML={{ __html: this.props.message}} />
      </div>
    );
  }

  render() {
    return (
      <div>
        {this.renderError()}
        {this.renderMessage()}
      </div>
    );
  }
}

ErrorContainer.propTypes = {
  error: React.PropTypes.string,
  dispatch: React.PropTypes.func,
  message: React.PropTypes.string,
};

function mapStateToProps(state) {
  return {
    error: state.meta.get('error'),
    message: state.meta.get('message'),
  };
}

export default connect(mapStateToProps)(ErrorContainer);
