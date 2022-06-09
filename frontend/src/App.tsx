import React, {Suspense} from 'react';
import {Provider} from 'react-redux';

import './App.scss';

import TopBar from './components/TopBar';
import Sidebar from './components/Sidebar';
import MainContent from './components/MainContent';
import Store from './store';
import {Box} from '@mui/material';
import {ThemeProvider} from '@mui/material/styles';
import Theme from './util/Theme';

/**
 * This is the root element of the React application. It divides the main screen area into the three main components.
 * The top bar, the sidebar and the main content area.
 */
export default function App(): JSX.Element {
  return (
    <Suspense fallback='loading'>
      <Provider store={Store}>
        <ThemeProvider theme={Theme}>
          <Box id='app' display='flex' flexDirection='column' style={{height: '100%'}}>
            <TopBar />
            <Box display='flex' flexDirection='row' flexGrow={1} alignItems='stretch'>
              <Sidebar />
              <MainContent />
            </Box>
          </Box>
        </ThemeProvider>
      </Provider>
    </Suspense>
  );
}
