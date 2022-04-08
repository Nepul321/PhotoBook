import { LikeUnlike } from "../lookups";
import numeral from 'numeral'

function Like(props) {
  const { post } = props;
  function HandleClick(id, action) {
    LikeUnlike(id, action, (response, status) => {
      if (status === 200) {
        return
      } else if(status === 401) {
        alert("Necessary data not given")
      } else if(status === 403) {
        alert("Login")
        window.location.href = "/accounts/login/?next=/"
      } else if(status === 404) {
        alert("Post not found")
      } else if (status === 500) {
        alert("Please try again")
      }
    })


  }
  return (
    <button
      className="btn btn-primary"
      onClick={() => HandleClick(post.id, "like")}
    >
      Likes {numeral(post.likes).format("0a")}
    </button>
  );
}

export default Like;
