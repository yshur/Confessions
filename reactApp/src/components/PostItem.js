import React, { Component } from 'react';
import './chart.css';
import axios from 'axios'

class PostItem extends Component {
  constructor(){
    super();
    this.state = {
      postsArray: []
    }
    this.add = this.add.bind(this)
    this.eachPost = this.eachPost.bind(this)
    this.eachissue = this.eachissue.bind(this)
  }
  componentDidMount() {
    var url = 'https://collegeconffessions.herokuapp.com/getRandomPosts';
    // console.log(url)
    axios.get(url)
      .then((res) => {
        // console.log(res)
        var self=this;
        res.data.map((Post) => {
                self.add(Post)
                // console.log(Issues)
              });
     })
}

  add(Post) {
      console.log(Post);
      this.setState(prevState => ({
        postsArray: [
          ...prevState.postsArray,
            Post
          ]
      }));
    }
    eachissue(issue) {
      console.log(issue)
      return (
        <span>{issue},</span>
      )
    }
    eachPost(post) {
      console.log(post)
      return (
        <tr>
          <td>
            {post.time.substr(0, 10)}
          </td>
          <td>
            {post.college}
          </td>
          <td>
            {post.likes}
          </td>
          <td>
            {post.content}
          </td>
          <td>
            <span>{post.issues.map(this.eachissue)}</span>
          </td>
        </tr>
      )
    }
    render() {
      return <div>
        <h1> ... והנה כמה פוסטים רנדומליים לדוגמא </h1>
        <table><thead><tr><th>תאריך</th><th>מוסד אקדמי</th>
        <th>כמות לייקים</th><th>תוכן הפוסט</th><th>רשימת נושאים</th></tr></thead><tbody>
        {this.state.postsArray.map(this.eachPost)}
      </tbody></table></div>;
  }
}



export default PostItem;
