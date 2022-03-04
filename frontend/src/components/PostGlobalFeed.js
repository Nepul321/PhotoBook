import {useState, useEffect} from 'react'
import {backend, getCookie} from '../lookups'
function PostFeed() {
    const [posts, setposts] = useState([]);
    useEffect(() => {
        fetch(`${backend}/posts/global/`)
        .then(res => {
            return res.json();
        })

        .then(data => {
            setposts(data);
        })
    })
    return (
        <div className="container-fluid my-5">
            <h1>PhotoBook</h1>
            {posts.map((item, key) => {
                return (
                    <div class="card mb-3">
                    <div class="row g-0">
                   <div class="col-md-4">
                   <img src={item.image} class="img-fluid rounded-start" alt="" />
                   </div>
                   <div class="col-md-8">
                   <div class="card-body">
                       <h5 className='card-text'>@{item.user.username}</h5>
                       <p class="card-text">{item.caption}</p>
                       <p class="card-text my-3"><small class="text-muted">{item.date}</small></p>
                       <a href="" class="btn btn-outline-primary">View post</a>
                   </div>
                   </div>
               </div>
               </div>
                )
            })}
        </div>
    )
}

export default PostFeed;