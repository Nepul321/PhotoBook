import {Routes, Route} from 'react-router-dom'
import Home from './pages/Home';
import UserPostFeed from './pages/UserPostFeed'
import PostDetail from './pages/PostDetail';
import Profile from './pages/Profile';
import Search from './pages/Search';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" exact element={<Home />}></Route>
        <Route path="/feed" exact element={<UserPostFeed />}></Route>
        <Route path="/posts/:id" exact element={<PostDetail />}></Route>
        <Route path="/u/:username" exact element={<Profile />}></Route>
        <Route path="/search" exact element={<Search />}></Route>
      </Routes>
    </div>
  );
}

export default App;
