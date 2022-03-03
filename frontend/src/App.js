import {Routes, Route} from 'react-router-dom'
import Home from './pages/Home';
import PostCreate from './pages/PostCreate';
import UserPostFeed from './pages/UserPostFeed'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" exact element={<Home />}></Route>
        <Route path="/create" exact element={<PostCreate />}></Route>
        <Route path="/feed" exact element={<UserPostFeed />}></Route>
      </Routes>
    </div>
  );
}

export default App;
