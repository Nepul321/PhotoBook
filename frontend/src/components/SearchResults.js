import Post from './Post'

function SearchResults(props) {
  const {results} = props
  return (
      <div className="results my-5">
          {results.map((item, key) => {
              return <Post post={item} key={key} showLikeButtons={false}/>
          })}
      </div>
  )
}

export default SearchResults;