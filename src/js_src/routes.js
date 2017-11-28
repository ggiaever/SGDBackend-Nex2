import React  from 'react';
import { IndexRoute, Route  } from 'react-router';

// unauthenticated routes and layout
import Layout from './containers/layout';
import PublicHome from './containers/publicHome';
// import ColleaguesIndex from './containers/colleagues/index';
// import ColleaguesShow from './containers/colleagues/show';
import Help from './containers/help';
import GoogleLogin from './containers/googleLogin';
// authenticated curate inputs
import { requireAuthentication } from './containers/authenticateComponent';
// import CurateLayout from './containers/curateHome/layout';
import CurateHome from './containers/curateHome';
import Search from './containers/search';
import LocusShow from './containers/locus/show';
import TriageIndex from './containers/triage';
import SpreadsheetUpload from './containers/spreadsheetUpload/index';
import Settings from './containers/settings/index';
// curate lit biz
import Blank from './components/blank';
import CurateLit from './containers/curateLit/layout';
import CurateLitBasic from './containers/curateLit/basic';
import CurateLitPhenotype from './containers/curateLit/phenotype';
// import CurateLitOverview from './containers/curateLit/index';
// public interfaces with no layout
import PublicLayout from './containers/layout/PublicLayout';
import AuthorResponse from './containers/authorResponse/index';
import NewColleague from './containers/colleagues/new';
import EditColleague from './containers/colleagues/edit';
import NewGeneNameReservation from './containers/reserve/index';

// <Route component={requireAuthentication(SpreadsheetUpload)} path='spreadsheet_upload' />
// <IndexRoute component={requireAuthentication(CurateHome)} />
export default (
  <Route>
    <Route component={Layout} path='/'>
      <IndexRoute component={requireAuthentication(CurateHome)} />
      <Route component={requireAuthentication(TriageIndex)} path='triage' />
      <Route component={requireAuthentication(SpreadsheetUpload)} path='spreadsheet_upload' />
      <Route component={requireAuthentication(Settings)} path='settings' />
      <Route component={Help} path='help' />
      <Route component={requireAuthentication(Search)} path='search' />
      <Route component={PublicHome} path='login' />
      <Route component={GoogleLogin} path='google_login' />
      <Route component={requireAuthentication(LocusShow)} path='curate/locus/:id' />
      <Route component={requireAuthentication(CurateLit)} path='curate/reference/:id'>
        <IndexRoute component={requireAuthentication(CurateLitBasic)} />
        <Route component={requireAuthentication(Blank)} path='protein' />
        <Route component={requireAuthentication(CurateLitPhenotype)} path='phenotypes' />
        <Route component={requireAuthentication(Blank)} path='go' />
        <Route component={requireAuthentication(Blank)} path='datasets' />
        <Route component={requireAuthentication(Blank)} path='regulation' />
        <Route component={requireAuthentication(Blank)} path='interaction' />
      </Route>
    </Route>
    <Route component={PublicLayout}>
        <Route component={AuthorResponse} path='author_response' />
        <Route component={NewColleague} path='new_colleague' />
        <Route component={EditColleague} path='colleague/:formatName/edit' />
        <Route component={NewGeneNameReservation} path='new_reservation' />
      </Route>
  </Route>
);
