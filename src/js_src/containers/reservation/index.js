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
        'Status': 'Unprocessed',
        'Reservation Date': 'n/a',
        'Expiration Date': 'n/a',
        'Reference': 'Fox T (2016)',
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
