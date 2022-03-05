import {useState, useEffect} from 'react'
import {useParams} from 'react-router-dom'
import {backend} from '../lookups'
import Like from '../components/Like'
import UnLike from '../components/Unlike'

function PostDetail() {
    const [post, setPost] = useState({});
    const {id} = useParams();

    useEffect(() => {
        fetch(`${backend}/posts/${id}/`)
        .then(res => {
            if(res.status === 200) {
                return res.json()
            } else if(res.status === 403) {
              alert("You don't have access to view this post")
              window.location.href = '/feed/'
            } else if(res.status === 404) {
                alert("Post not found")
                window.location.href = '/feed/'
            } else if(res.status === 500) {
                alert("An error occurred. Please try again.")
            }
            
            return {}
        })

        .then(data => {
           setPost(data)
        })
    })

    return (
        <div className="container my-4">
            <img src={post.image} style={{height : 'auto', width : '100%'}} alt=""/>
            <hr />
            <p>{post.caption}</p>
            <div className='btn-group'>
                <Like post={post}/>
                <UnLike post={post} />
            </div>
            <div className='back my-3'>
            <a href='/feed/' className='btn btn-outline-primary'>Back</a>
            </div>
        </div>
    )
}

export default PostDetail;