import Like from "./Like";
import UnLike from "./Unlike";
import ReactMarkdown from 'react-markdown'

function Post(props) {
  const { post } = props;
  const post_detail_url = `/posts/${post.id}/`
  return (
    <div className="card mb-3">
      <div className="row g-0">
        <div className="col-md-4">
          <img src={post.image} className="img-fluid rounded-start" alt="" />
        </div>
        <div className="col-md-8">
          <div className="card-body">
            <h5 className="card-text">@{post.user.username}</h5>
            <ReactMarkdown>{post.caption}</ReactMarkdown>
            <p className="card-text my-3">
              <small className="text-muted">{post.date}</small>
            </p>
            <div className="btn-group">
            <Like post={post}/>
            <UnLike post={post} />    
            </div>
            <div className="link my-4">
            <a href={post_detail_url} className="btn btn-outline-primary">
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