import React, { Component } from 'react';
import Home  from './components/home';
import Footer  from './components/footer';

class App extends Component {
  render() {
    return (
      <div className="mainWrapper">
        <Home />
        <Footer />
      </div>
    );
  }
}

export default App;
