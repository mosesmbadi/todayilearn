import React, { Component } from 'react';

class Home extends Component {
    state = {
        blogs: []
      };
    
      async componentDidMount() {
        try {
          const res = await fetch('http://127.0.0.1:8000/api/');
          const blogs = await res.json();
          this.setState({
            blogs
          });
        } catch (e) {
          console.log(e);
        }
      }
    

  render() {
    return (
        <div>
            {this.state.blogs.map(item => (
            <div key={item.id}>
                <div class="row">
                <div class="col-sm-6">
                    <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{item.title}</h5>
                        <p class="card-text">{item.body}</p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            ))}
        </div>
    );
  }
}

export default Home;

