import Like from "./Like";
import UnLike from "./Unlike";
import ReactMarkdown from 'react-markdown'
import PostProfileBadge from "./PostProfileBadge";

function LikeUnlike(props) {
  const {post} = props;
  return (
    <div className="btn-group">
    <Like post={post}/>
    <UnLike post={post} />    
    </div>
  )
}

function Post(props) {
  const { post } = props;
  const { showLikeButtons } = props;
  const post_detail_url = `/posts/${post.id}/`
  return (
    <div className="card mb-3">
      <div className="row g-0">
        <div className="col-md-4">
          <img src={post.image} className="img-fluid rounded-start" alt="" />
        </div>
        <div className="col-md-8">
          <div className="card-body">
            <PostProfileBadge post={post}/>
            <ReactMarkdown>{post.caption}</ReactMarkdown>
            {showLikeButtons === true ? (
             <LikeUnlike post={post}/>
            ) : null}
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