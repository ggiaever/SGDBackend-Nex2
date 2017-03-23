import React, { Component } from 'react';

import ProgressTracker from '../../components/progressTracker';
// import ReferenceForm from '../../components/referenceForm';
// import BasicReservationInfo from './basicReservationInfo';
// import BasicColleagueInfo from './basicColleagueInfo';
import GeneNameReservationSummary from '../../components/geneNameReservationSummary';

class NewGeneNameReservation extends Component {
  render() {
    return (
      <div>
        <h1>Reserve a Gene Name</h1>
        <ProgressTracker currentStep={3} steps={STEPS} />
        <GeneNameReservationSummary />
      </div>
    );
  }
}

const STEPS = [
  'Basic Information',
  'Your Information',
  'Reference Information',
  'Submit'
];

export default NewGeneNameReservation;
