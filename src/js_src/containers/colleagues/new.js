import React, { Component } from 'react';

import ColleagueFormShow from '../../components/colleagues/colleagueFormShow';

class Colleagues extends Component {
  render() {
    return (
      <div>
        <ColleagueFormShow
          isReadOnly isCurator={false} 
        />
      </div>
    );
  }
}

export default Colleagues;
