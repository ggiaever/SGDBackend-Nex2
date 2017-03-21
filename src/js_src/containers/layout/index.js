import React, { Component, PropTypes } from 'react';
import { Link } from 'react-router';
import { connect } from 'react-redux';

// import * as AuthActions from '../actions/auth_actions';
import style from './style.css';
import SearchBar from './searchBar';
import ErrorContainer from './errorContainer';
import curateLogo from './curateLogo.png';

class LayoutComponent extends Component {
  renderAuthedMenu() {
    return (
      <div>
        <ul className={`menu ${style.authMenu}`}>
          <li><a className={style.navLink} href='/'>
            <i className='fa fa-sign-out' /> Logout</a>
          </li>
          <li><SearchBar /></li>
        </ul>
      </div>
    );
  }
  
  render() {
    // init auth nodes, either login or logout links
    let authNodes = this.props.isAuthenticated ? this.renderAuthedMenu() : null;
    return (
      <div>
        <ErrorContainer />
        <div className='row'>
          <div className='columns small-12'>
            <Link className={style.indexLink} to='curate'>
              <img className={style.imgLogo} src={curateLogo} /><i>Saccharomyces</i> Genome Database <span className='label'>Curator</span>
            </Link>
          </div>
        </div>
        <nav className={`top-bar ${style.navWrapper}`}>
          <div className='top-bar-left'>
            <ul className={`menu ${style.topMenu}`}>
              <li>
                <Link to='curate'>
                  <span><i className='fa fa-home' /> Home</span>
                </Link>
              </li>
              <li>
                <Link to='help'>
                  <span><i className='fa fa-question-circle' /> Help</span>
                </Link>
              </li>
            </ul>
          </div>
          <div className='top-bar-right'>
            {authNodes}
          </div>
        </nav>
        <div className={`row ${style.contentRow}`}>
          <div className={`large-12 columns ${style.contentContainer}`}>
            {this.props.children}
          </div>
        </div>
      </div>
    );
  }
}

LayoutComponent.propTypes = {
  children: PropTypes.node,
  isAuthenticated: React.PropTypes.bool
};

function mapStateToProps(state) {
  return {
    isAuthenticated: state.auth.get('isAuthenticated')
  };
}

export { LayoutComponent as LayoutComponent };
export default connect(mapStateToProps)(LayoutComponent);
