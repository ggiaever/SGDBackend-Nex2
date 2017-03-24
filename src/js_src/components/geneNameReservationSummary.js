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
          <a>Sheppard TK, et al. (2016) The Saccharomyces Genome Database Variant Viewer. Nucleic Acids Res 44(D1):D698-702</a>
        </div>
      </div>
    );
  }
}

export default GeneNameReservationSummary;
