import React, { Component } from 'react';

import ProgressTracker from '../../components/progressTracker';

class NewGeneNameReservation extends Component {
  render() {
    return (
      <div>
        <h1>Reserve a Gene Name</h1>
        <ProgressTracker currentStep={0} steps={STEPS} />
      </div>
    );
  }
}

const STEPS = [
  'Basic Information',
  'Your Information',
  'Reference Information'
];

export default NewGeneNameReservation;
