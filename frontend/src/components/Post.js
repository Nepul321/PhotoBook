import Like from "./Like";
import UnLike from "./Unlike";

function Post(props) {
  const { post } = props;
  return (
    <div className="card mb-3">
      <div className="row g-0">
        <div className="col-md-4">
          <img src={post.image} className="img-fluid rounded-start" alt="" />
        </div>
        <div className="col-md-8">
          <div className="card-body">
            <h5 className="card-text">@{post.user.username}</h5>
            <p className="card-text">{post.caption}</p>
            <p className="card-text my-3">
              <small className="text-muted">{post.date}</small>
            </p>
            <div className="btn-group">
            <Like post={post}/>
            <UnLike post={post} />    
            </div>
            <div className="link my-4">
            <a href="" className="btn btn-outline-primary">
              View post
            </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Post;