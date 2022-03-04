import {useState, useEffect} from 'react';
import {backend} from '../lookups'
import Post from './Post';

function UserPostFeedList() {
    const [posts, setPosts] = useState([]);
    useEffect(() => {
        fetch(`${backend}/posts/feed/`)
        .then(res => {
            return res.json()
        })

        .then(data => {
            setPosts(data)
        })
    })
    return (
        <div className='container-fluid my-5'>
            <h1>Your feed</h1>
            {posts === [] ? <p>Loading...</p> :
                posts.map((item, key) => {
                    return (
                       <Post post={item} key={key}/>
                    )
                })
            }
        </div>
    )
}

export default UserPostFeedList;