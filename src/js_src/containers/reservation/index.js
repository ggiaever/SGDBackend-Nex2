import React, { Component } from 'react';
import _ from 'underscore';

import Table from '../../components/table';

class GeneNameReservationIndex extends Component {
  render() {
    // TEMP example data
    let reservations = [
      {
        'Proposed name': {
          name: 'xyz123',
          href: '/curate/reservations/123'
        },
        'ORF': 'YHR214W',
        'Reference': 'Eustice M and Pillus L (2014) Unexpected Function of the Glucanosyltransferase Gas1 in the DNA Damage Response Linked to Histone H3 Acetyltransferases in Saccharomyces cerevisiae. Genetics 196(4):1029-39',
      }
    ];
    let _fields = _.keys(reservations[0]);
    return (
      <div>
        <h1>Gene Name Reservations</h1>
        <Table entries={reservations} fields={_fields} />
      </div>
    );
  }
}

export default GeneNameReservationIndex;
