import Comment from "./Comment";
import {useEffect, useState} from 'react'
import { backend } from "../lookups";

function CommentSection(props) {
    const {post} = props
    const [comments, setComments] = useState([]);
    useEffect(() => {
      fetch(`${backend}/comments/posts/${post.id}/`)
      .then(res => {
          return res.json();
      })

      .then(data => {
        setComments(data);
      })
    })

    console.log(comments)
    function handleFormSubmit(e) {
       e.preventDefault();
       e.target.reset()
    }
    return (
        <div className="comment-section">
          <form id="create" onSubmit={handleFormSubmit}>
             <textarea className="form-control" placeholder="Write a comment"></textarea>
             <button className="btn my-2 text-white" style={{backgroundColor : "#487eb0"}}>Comment</button>
          </form>
          <div className="comments my-3">
          {comments.map((item, key) => {
            return <Comment comment={item} key={key}/>
          })}
          </div>
        </div>
    )
}

export default CommentSection;