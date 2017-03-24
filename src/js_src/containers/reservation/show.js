import React, { Component } from 'react';

import GeneNameReservationSummary from '../../components/geneNameReservationSummary';

class ShowGeneNameReservation extends Component {
  render() {
    return (
      <div>
        <h1>XYZ123 / YHR218W</h1>
        <span><a><i className='fa fa-edit' /> Edit</a></span>
        <GeneNameReservationSummary />
      </div>
    );
  }
}

export default ShowGeneNameReservation;
