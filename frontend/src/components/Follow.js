import { FollowUnFollow } from "../lookups";

function Follow(props) {
  const { profile } = props;
  function handleClick(username, action) {
    FollowUnFollow(username, action, (response, status) => {
      if (status === 200) {
        return;
      } else if (status === 403) {
        alert(response.detail);
        window.location.href = "/accounts/login/?next=/feed/";
      } else if (status === 404) {
        alert(response.detail);
        window.location.href = "/feed/";
      } else if (status === 500) {
        alert("An error occurred");
      }
    });
  }
  return (
    <button
      className="btn btn-primary"
      onClick={() => handleClick(profile.user.username, "follow")}
    >
      Follow
    </button>
  );
}

export default Follow;
