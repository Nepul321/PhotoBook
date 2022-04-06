import Comment from "./Comment";
import { useEffect, useState, useRef } from "react";
import { backend } from "../lookups";
import { CommentCreate } from "../lookups";

function CommentSection(props) {
  const { post } = props;
  const content_ref = useRef();
  const [comments, setComments] = useState([]);
  useEffect(() => {
    fetch(`${backend}/comments/posts/${post.id}/`)
      .then((res) => {
        return res.json();
      })

      .then((data) => {
        setComments(data);
      });
  });
  function handleFormSubmit(e) {
    e.preventDefault();
    const content = content_ref.current.value;
    CommentCreate(post.id, content, null, (response, status) => {
      if (status === 404) {
        alert(response.detail);
      } else if (status === 401) {
        alert("Required data not provided");
      } else if (status === 403) {
        alert("Login");
        window.location.href = "/accounts/login/?next=/";
      } else if (status === 500) {
        alert("An error occurred please try again");
      } else if (status === 201) {
        return;
      }
    });
    e.target.reset();
  }
  return (
    <div className="comment-section">
      <form id="create" onSubmit={handleFormSubmit}>
        <textarea
          className="form-control"
          placeholder="Write a comment"
          ref={content_ref}
        ></textarea>
          <button
            className="btn my-2 text-white"
            style={{ backgroundColor: "#487eb0" }}
          >
            Comment
          </button>
          <p className="text-danger">** You can use markdown in comments and replies</p>
      </form>
      <div className="comments my-3">
        {comments.map((item, key) => {
          return <Comment comment={item} key={key} />;
        })}
      </div>
    </div>
  );
}

export default CommentSection;
