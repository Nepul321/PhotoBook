import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";

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
      {children.length < 1 ? null : (
        <button
          className="btn btn-outline-secondary"
          onClick={handleShowReplies}
        >
          {verb} replies ({children.length})
        </button>
      )}

      {!showReplies ? null : <Replies replies={children} />}
    </div>
  );
}

export default Comment;
