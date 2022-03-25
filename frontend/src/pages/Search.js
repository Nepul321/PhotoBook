import { useState, useRef } from "react";
import { backend } from "../lookups";
import SearchResults from "../components/SearchResults";

function Search() {
  const [results, setResults] = useState([]);
  const searchInput = useRef();

  function search(query) {
    let searched = query.trim()
    fetch(`${backend}/posts/search?q=${searched}`)
    .then((res) => {
        if (res.status === 200) {
            return res.json()
        } else if(res.status === 401) {
            alert("Nothing searched")
        } else if(res.status === 500) {
            alert("An error occurred. Please try again.")
        }
    })

    .then((data) => {
        setResults(data);
    })

    console.log(results)
  }

  function searchOnInput() {
    const searching = searchInput.current.value

    if (searching === "") {
      setResults([]);
    }
    if (searching !== "") {
        search(searching)
    }

  }

  function searchOnSubmit(e) {
    e.preventDefault();
    const searched = searchInput.current.value
    if (searched !== "") {
        search(searched)
   }
  }
  return (
    <div className="container-fluid my-5">
      <h1>Search</h1>
      <form id="search" onSubmit={searchOnSubmit}>
        <div className="input-group">
          <input
            type="text"
            className="form-control"
            required
            placeholder="Search"
            ref={searchInput}
            onInput={searchOnInput}
          />
          <button className="btn btn-primary">Search</button>
        </div>
      </form>
   <SearchResults results={results}/>
    </div>
  );
}

export default Search;
