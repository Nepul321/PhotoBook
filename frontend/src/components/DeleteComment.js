import { CommentDelete } from "../lookups";

function DeleteComment(props) {
    const {comment} = props
    function handleDelete() {
       CommentDelete(comment.id, (response, status) => {
            if(status === 403) {
                alert(response.detail)
            } else if(status === 404) {
                alert(response.detail)
            } else if(status === 200) {
                alert(response.detail)
            } else if(status === 401) {
               alert("Required data not provided")
            } else if(status === 500) {
                alert("An error occurred please try again")
            }
       })
    }
    return (
        <button className="btn btn-outline-danger" onClick={handleDelete}>Delete</button>
    )
}

export default DeleteComment;