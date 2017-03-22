import React, { Component } from 'react';

import ProgressTracker from '../../components/progressTracker';
// import BasicReservationInfo from './basicReservationInfo';
import BasicColleagueInfo from './basicColleagueInfo';

class NewGeneNameReservation extends Component {
  render() {
    return (
      <div>
        <h1>Reserve a Gene Name</h1>
        <ProgressTracker currentStep={1} steps={STEPS} />
        <BasicColleagueInfo />
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
