import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { backend } from "../lookups";
import Like from "../components/Like";
import UnLike from "../components/Unlike";
import { DeletePost } from "../lookups";

function Actions(props) {
  const { post } = props;
  const [showpopup, setshowpopup] = useState(false);

  function handlepopupvisibility() {
    if (!showpopup) {
      setshowpopup(true);
    }

    if (showpopup) {
      setshowpopup(false);
    }
  }

  function deletePost(id) {
    DeletePost(id, (response, status) => {
        console.log(response.detail, status)
        if (status === 200) {
            alert(response.detail)
            window.location.href = '/feed/'
        } else if(status === 403) {
            if(response.error === 1) {
                alert(response.detail)
            } else {
                alert("login")
                window.location.href = '/accounts/login/?next=/'
            }
        } else if(status === 500) {
            alert("An error occurred. Please try again.")
        } else if(status === 404) {
            alert(response.detail)
        } else if(status === 401) {
            alert(response.detail)
        } else if(status === 400) {
            alert(response.detail)
        } 
    })
  }
  return (
    <div className="actions my-3">
      {showpopup && (
        <div className="card mb-4">
          <div className="card-body">
            <p>Are you sure you want to delete this post ?</p>
            <div className="btn-group my-2">
              <button
                className="btn btn-outline-primary btn-sm"
                onClick={handlepopupvisibility}
              >
                Cancel
              </button>
              <button
                className="btn btn-outline-danger btn-sm"
                onClick={() => deletePost(post.id)}
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
      <div className="btn-group">
        <a href={`/posts/${post.id}/update/`} className="btn btn-secondary">
          Update
        </a>
        <button className="btn btn-danger" onClick={handlepopupvisibility}>
          Delete
        </button>
      </div>
    </div>
  );
}

function PostDetail() {
  const [post, setPost] = useState({});
  const { id } = useParams();

  useEffect(() => {
    fetch(`${backend}/posts/${id}/`)
      .then((res) => {
        if (res.status === 200) {
          return res.json();
        } else if (res.status === 403) {
          alert("You don't have access to view this post");
          window.location.href = "/feed/";
        } else if (res.status === 404) {
          window.location.href = "/feed/";
        } else if (res.status === 500) {
          alert("An error occurred. Please try again.");
        }

        return {};
      })

      .then((data) => {
        setPost(data);
      });
  });

  return (
    <div className="container my-4">
      <img src={post.image} style={{ height: "auto", width: "100%" }} alt="" />
      <hr />
      <p>{post.caption}</p>
      <div className="btn-group">
        <Like post={post} />
        <UnLike post={post} />
      </div>
      {post.is_owner === true ? <Actions post={post} /> : null}
      <div className="back my-3">
        <a href="/feed/" className="btn btn-outline-primary">
          Back
        </a>
      </div>
    </div>
  );
}

export default PostDetail;
