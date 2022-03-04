import {useState, useEffect} from 'react'
import {backend, getCookie} from '../lookups'
import Post from '../components/Post'

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
                   <Post post={item} key={key}/>
                )
            })}
        </div>
    )
}

export default PostFeed;