import {Routes, Route} from 'react-router-dom'
import Home from './pages/Home';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" exact element={<Home />}></Route>
      </Routes>
    </div>
  );
}

export default App;
