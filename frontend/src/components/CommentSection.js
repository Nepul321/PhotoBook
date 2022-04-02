import Comment from "./Comment";

function CommentSection() {
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
          <div className="comments">
         <Comment />
          </div>
        </div>
    )
}

export default CommentSection;