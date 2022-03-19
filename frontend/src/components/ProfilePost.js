

function ProfilePost(props) {
  const { post } = props;
  return (
    <div className="col-sm mb-3">
        <a href={`/posts/${post.id}/`}>
        <img src={post.image} style={{width : '18rem'}} alt=""/>
        </a>
    </div>
  );
}

export default ProfilePost;
