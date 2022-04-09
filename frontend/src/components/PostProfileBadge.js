function ProfilePic(props) {
  const { post } = props;
  return (
    <p>
      <div className="profile-pic">
        <img
          src={post.user.profile_pic_url}
          style={{ height: "40px", width: "40px", borderRadius: "50%" }}
          alt=""
        />
        <a href={`/u/${post.user.username}/`} style={{ marginLeft: "10px" }}>
          {post.user.name}
        </a> - 
        <small className="text-muted"> {post.date}</small>
      </div>
    </p>
  );
}

function NoProfilePic(props) {
  const { post } = props;
  return (
    <p>
      <div
        style={{
          width: "40px",
          backgroundColor: "gray",
          color: "white",
          height: "40px",
          borderRadius: "50%",
          textAlign: "center",
          justifyContent: "center",
          alignItems: "center",
          display: "flex",
        }}
      >
        {post.user.username[0]}
      </div>
      <a href={`/u/${post.user.username}/`}>{post.user.name}</a> - <small className="text-muted"> {post.date}</small>
    </p>
  );
}

function PostProfileBadge(props) {
  const { post } = props;
  return (
    <div className="post-profile-badge">
      {post.user.profile_pic_url === null ? (
        <NoProfilePic post={post} />
      ) : (
        <ProfilePic post={post} />
      )}
    </div>
  );
}

export default PostProfileBadge;
