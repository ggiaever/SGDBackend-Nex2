import React, { Component } from 'react';
import { Link } from 'react-router';

class Table extends Component {
  formatHeader(d) {
    return d;
  }

  renderHeader() {
    let headerNodes = this.props.fields.map( (d,i) => {
      return <th key={'th' + i}>{this.formatHeader(d)}</th>;
    });
    return (
      <thead>
        <tr>{headerNodes}</tr>
      </thead>
    );
  }

  renderValue(d) {
    // render simple value for string
    if (typeof d === 'string') return d;
    // render a link
    return <Link to={d.href}>{d.name}</Link>;
  }

  renderSingleEntry(entry, entryI) {
    let nodes = this.props.fields.map( (d, i) => {
      let data = entry[d];
      return <td key={`td${entryI}.${i}`}>{this.renderValue(data)}</td>;
    });
    return (
      <tr key={'tr' + entryI}>
        {nodes}
      </tr>
    );
  }

  renderBody() {
    let rowNodes = this.props.entries.map(this.renderSingleEntry.bind(this));
    return (
      <tbody>
        {rowNodes}
      </tbody>
    );
  }

  render() {
    return (
      <div>
        <table>
          {this.renderHeader()}
          {this.renderBody()}
        </table>
      </div>
    );
  }
}

Table.propTypes = {
  entries: React.PropTypes.array,
  fields: React.PropTypes.array
};

export default Table;
