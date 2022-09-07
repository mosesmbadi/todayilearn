//component to render our blog list

import React from 'react'

const Articles = ({ articles }) => {
  return (
    <div>
      <center><h1>Blog List</h1></center>
      {articles.map((article) => (
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{article.name}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{article.username}</h6>
            <p class="card-text">{article.email}</p>
          </div>
        </div>
      ))}
    </div>
  )
};

export default Articles
