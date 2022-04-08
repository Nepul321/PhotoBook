import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import DeleteComment from "./DeleteComment";
import { CommentCreate } from "../lookups";
import numeral from "numeral";

function Replies(props) {
  const { replies } = props;

  return (
    <div className="container">
      {replies.map((comment, key) => {
        return (
          <div className="reply border my-3 p-3" key={key}>
            <p>
              <div
                style={{
                  width: "40px",
                  backgroundColor: "gray",
                  color: "white",
                  height: "40px",
                  borderRadius: "50%",
                  textAlign: "center",
                  justifyContent: "center",
                  alignItems: "center",
                  display: "flex",
                }}
              >
                {comment.user.username[0]}
              </div>
              <a href={`/u/${comment.user.username}/`}>{comment.user.name}</a> -
              {comment.date}
            </p>
            <ReactMarkdown>{comment.content}</ReactMarkdown>
            {comment.is_user === true ? <DeleteComment comment={comment}/> : null}
          </div>
        );
      })}
    </div>
  );
}

function Comment(props) {
  const [children, setChildren] = useState([]);
  const [showReplies, setShowReplies] = useState(false);
  const [verb, setVerb] = useState("Show");
  const { comment } = props;
  const content_ref = useRef();
  useEffect(() => {
    setChildren(comment.children);
  }, [comment.children]);
  function handleShowReplies() {
    if (showReplies === true) {
      setShowReplies(false);
      setVerb("Show");
    }

    if (showReplies === false) {
      setShowReplies(true);
      setVerb("Hide");
    }
  }

  function handleFormSubmit(e) {
    e.preventDefault();
    const content = content_ref.current.value;
    CommentCreate(comment.post.id, content, comment.id, (response, status) => {
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
        setShowReplies(true);
        setVerb("Hide");
      }
    });
    e.target.reset();
  }
  return (
    <div className="comment mb-3 border-bottom p-3">
      <p>
        <div
          style={{
            width: "40px",
            backgroundColor: "gray",
            color: "white",
            height: "40px",
            borderRadius: "50%",
            textAlign: "center",
            justifyContent: "center",
            alignItems: "center",
            display: "flex",
          }}
        >
          {comment.user.username[0]}
        </div>
        <a href={`/u/${comment.user.username}/`}>{comment.user.name}</a> -
        {comment.date}
      </p>
      <ReactMarkdown>{comment.content}</ReactMarkdown>
      <div className="btn-group">
      {comment.is_user === true ? <DeleteComment comment={comment}/> : null}
      {children.length < 1 ? null : (
        <button
          className="btn btn-outline-secondary"
          onClick={handleShowReplies}
        >
          {verb} replies ({numeral(children.length).format('0a')})
        </button>
      )}
      </div>

      <div className="container my-2">
      <form onSubmit={handleFormSubmit}>
        <textarea
          className="form-control"
          placeholder="Write a reply"
          ref={content_ref}
        ></textarea>
          <button
            className="btn my-2 text-white"
            style={{ backgroundColor: "#487eb0" }}
          >
            Reply
          </button>
      </form>
      </div>

      {!showReplies ? null : <Replies replies={children} />}
    </div>
  );
}

export default Comment;
