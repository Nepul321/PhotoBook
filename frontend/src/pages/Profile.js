import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { backend } from "../lookups";
import Follow from "../components/Follow";
import Unfollow from "../components/Unfollow";
import ProfilePost from "../components/ProfilePost";

function ProfilePosts(props) {
  const { posts } = props;
  console.log(posts);
  return posts.map((item, key) => {
    return <ProfilePost post={item} key={key} />;
  });
}

function Profile() {
  const [profile, setProfile] = useState(null);
  const [userPosts, setUserPosts] = useState([]);
  const { username } = useParams();
  useEffect(() => {
    fetch(`${backend}/profiles/${username}/`)
      .then((res) => {
        if (res.status === 200) {
          return res.json();
        } else if (res.status === 404) {
          window.location.href = "/feed/";
        } else if (res.status === 500) {
          alert("An error occurred. Please try again.");
        }

        return null;
      })

      .then((data) => {
        setProfile(data);
      });
  });

  useEffect(() => {
    fetch(`${backend}/profiles/${username}/posts/`)
      .then((res) => {
        if (res.status === 200) {
          return res.json();
        } else if (res.status === 404) {
          window.location.href = "/feed/";
        } else if (res.status === 500) {
          alert("An error occurred. Please try again.");
        }

        return null;
      })

      .then((data) => {
        setUserPosts(data);
      });
  });
  return (
    <div className="container-fluid my-5">
      {profile && (
        <div className="profile">
          <div className="card mb-3">
            <div className="row g-0">
              <div className="col-md-4">
                <img
                  src={profile.profile_pic}
                  className="img-fluid rounded-start"
                  alt=""
                />
              </div>
              <div className="col-md-8">
                <div className="card-body">
                  <h5 className="card-title">
                    {profile.user.name}
                    <p className="text-muted">(@{profile.user.username})</p>
                  </h5>
                  <p>Followers : {profile.followers}</p>
                  <p>Following : {profile.following}</p>
                  {!profile.is_following ? (
                    <Follow profile={profile} />
                  ) : (
                    <Unfollow profile={profile} />
                  )}
                  <p className="text-muted my-3">Joined on {profile.joined}</p>
                </div>
              </div>
            </div>
          </div>
          <div className="bio my-3">
            <h5 className="strong">Short bio</h5>
            <hr />
            <p className="lead">{profile.bio}</p>
          </div>
        </div>
      )}
      {userPosts === [] ? (
        <p>Loading</p>
      ) : (
        <div className="posts">
          <center>
          <h1>Posts</h1>
          <hr />
            <div className="row">
              <ProfilePosts posts={userPosts} />
            </div>
          </center>
        </div>
      )}
    </div>
  );
}

export default Profile;
