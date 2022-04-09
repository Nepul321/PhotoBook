function NoProfilePic(props) {
  const { comment } = props;
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
        {comment.user.username[0]}
      </div>
      <a href={`/u/${comment.user.username}/`} >{comment.user.name}</a> -
      {comment.date}
    </p>
  );
}

function ProfilePic(props) {
  const { comment } = props;
  return (
    <p>
      <div className="profile_pic">
        <img
          src={comment.user.profile_pic_url}
          style={{ height: "40px", width: "40px", borderRadius: "50%" }}
          alt=""
        />
        <a href={`/u/${comment.user.username}/`} style={{marginLeft : "10px"}}>{comment.user.name}</a> -
        {comment.date}
      </div>
    </p>
  );
}

function CommentProfileBadge(props) {
  const { comment } = props;
  return (
    <div className="profile-badge">
      {comment.user.profile_pic_url === null ? (
        <NoProfilePic comment={comment} />
      ) : (
        <ProfilePic comment={comment} />
      )}
    </div>
  );
}

export default CommentProfileBadge;
