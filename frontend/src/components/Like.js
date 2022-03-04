function Like(props) {
   const {post} = props
   return (
       <button className="btn btn-primary">Likes {post.likes}</button>
   )
}

export default Like;