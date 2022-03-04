import Like from "./Like";
import UnLike from "./Unlike";

function Post(props) {
  const { post } = props;
  return (
    <div class="card mb-3">
      <div class="row g-0">
        <div class="col-md-4">
          <img src={post.image} class="img-fluid rounded-start" alt="" />
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 className="card-text">@{post.user.username}</h5>
            <p class="card-text">{post.caption}</p>
            <p class="card-text my-3">
              <small class="text-muted">{post.date}</small>
            </p>
            <div className="btn-group">
            <Like post={post}/>
            <UnLike post={post} />    
            </div>
            <div className="link my-4">
            <a href="" class="btn btn-outline-primary">
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