import React, { Component } from 'react';
import Articles from './components/blog';

class App extends Component {
  render() {
    return (
        <Articles articles={this.state.articles} />
    )
}


  //creating state
  state = {
    articles: []
  }

  componentDidMount() {
    //this endpoint seem to work, need to fix one from django
    fetch('http://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then((data) => {
      this.setState({ articles: data })
    })
    .catch(console.log)
  }
}

export default App;