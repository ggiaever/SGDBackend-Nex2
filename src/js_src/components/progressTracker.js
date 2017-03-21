import React, { Component } from 'react';

import style from './style.css';

class ProgressTracker extends Component {
  renderLabels() {
    return this.props.steps.map( (d, i) => {
      return (
        <div key={`progLabel${i}`}>
          <div>{d}</div>
        </div>
      );
    });
  }


  renderSteps() {
    let current = this.props.currentStep || 0;
    return this.props.steps.map( (d, i) => {
      let isComplete = (i <= current);
      let classSuffix = isComplete ? style.completeTrackerNode : '';
      return (
        <div key={`prog${i}`}>
          <span className={`${style.progressTrackerNode} ${classSuffix}`} />
        </div>
      );
    });
  }

  render() {
    return (
      <div>
        <div className={style.progressTrackerContainer}>
          {this.renderLabels()}
        </div>
        <div className={style.progressTrackerContainer}>
          <div className={style.progressTrackerLine} />
          {this.renderSteps()}
        </div>
      </div>
    );
  }
}

ProgressTracker.propTypes = {
  currentStep: React.PropTypes.number,
  steps: React.PropTypes.array
};

export default ProgressTracker;
