import { LikeUnlike } from "../lookups";

function UnLike(props) {
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
        } else if (status === 500) {
          alert("Please try again")
        }
      })
  
      
    }
    return (
      <button
        className="btn btn-primary"
        onClick={() => HandleClick(post.id, "unlike")}
      >
        Unlike
      </button>
    );
  }
  
  export default UnLike;