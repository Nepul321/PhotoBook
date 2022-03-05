import {Routes, Route} from 'react-router-dom'
import Home from './pages/Home';
import UserPostFeed from './pages/UserPostFeed'
import PostDetail from './pages/PostDetail';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" exact element={<Home />}></Route>
        <Route path="/feed" exact element={<UserPostFeed />}></Route>
        <Route path="/posts/:id" exact element={<PostDetail />}></Route>
      </Routes>
    </div>
  );
}

export default App;
