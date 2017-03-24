import React, { Component } from 'react';

import style from './style.css';
import DetailList from './detailList';

class GeneNameReservationSummary extends Component {
  render() {
    let basicInfo = {
      'Proposed gene name': 'xyz123',
      'ORF name': 'YHR218W',
      'description of gene name acronym': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt',
      'Notes': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt'
    };
    let submitterInfo = {
      'name': 'Travis Sheppard',
      'phone': '(555) 555-1234',
      'email': 'tshepp@stanford.edu'
    };
    let statusInfo = {
      'Status': 'Reserved',
      'Reservation Date': '2017-03-24',
      'Expiration Date': '2018-03-24'
    };
    return (
      <div>
        <div className={style.paddedBottom}>
          <label>Gene name information</label>
          <DetailList data={basicInfo} />
        </div>
        <div className={style.paddedBottom}>
          <label>Submitter</label>
          <DetailList data={submitterInfo} />
        </div>
        <div className={style.paddedBottom}>      
          <label>Reference</label>
          <a>Fox T (2016)</a>
        </div>
        <div className={style.paddedBottom}>
          <label>Reservation Status</label>
          <DetailList data={statusInfo} />
        </div>
        <div className={style.splitButtonContainer}>
          <a className='button'>Promote Gene Name</a>
          <a className='button secondary'><i className='fa fa-trash' /> Discard</a>
        </div>
      </div>
    );
  }
}

export default GeneNameReservationSummary;
