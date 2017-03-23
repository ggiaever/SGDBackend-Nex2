import React, { Component } from 'react';
import { Async } from 'react-select';
import _ from 'underscore';

import fetchData from '../../lib/fetchData';

class MultiSelectField extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: []
    };
  }

  handleChange(newValue) {
    this.setState({ value: newValue });
  }

  // from a URL, returns the fetch function needed to get the options
  getAsyncOptions (input, cb) {
    let url = `${this.props.optionsUrl}${input}`;
    fetchData(url)
      .then( response => {
        let _options = response.results || [];
        let optionsObj = {
          options: _options,
          complete: true
        };
        // add defaultOptions to results and remove duplicated
        let defaultValues = this.props.defaultValues || [];
        optionsObj.options = _.uniq(optionsObj.options.concat(defaultValues));
        return cb(null, optionsObj);
      });
  }

  render () {
    let iconNode = this.props.iconClass ? <span><i className={`fa fa-${this.props.iconClass}`} /> </span> : null;
    return (
      <div className='selectContainer'>
        <label>{iconNode}{this.props.displayName}</label>
        <Async
          onChange={this.handleChange.bind(this)}
          name={this.props.paramName} value={this.state.value}
          loadOptions={this.getAsyncOptions.bind(this)}
          labelKey='name' valueKey='name'
          allowCreate
          cache={false} multi={this.props.multi}
        />
      </div>
    );
  }
}

MultiSelectField.propTypes = {
  displayName: React.PropTypes.string,
  optionsUrl: React.PropTypes.string,
  paramName: React.PropTypes.string,
  defaultValues: React.PropTypes.array,
  iconClass: React.PropTypes.string,
  defaultOptions: React.PropTypes.array,
  allowCreate: React.PropTypes.bool,
  multi: React.PropTypes.bool
};

export default MultiSelectField;
