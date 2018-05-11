import React, {Component} from 'react';
import { connect } from 'react-redux';
import CurateLayout from '../curateHome/layout';


class FileCurate extends Component{
  constructor(props){
    super(props);
  }

  render(){
    return (
      <CurateLayout>
        <div>
            <h1>File Curate</h1>
        </div>
      </CurateLayout>
    );
  }
}

function mapStateToProps(state){
  return {state:state};
}

export {FileCurate as FileCurate};
export default connect(mapStateToProps)(FileCurate);
