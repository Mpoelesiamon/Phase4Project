import React, { useState } from 'react';
import { Routes, Route,} from 'react-router-dom';
import NavigationBar from './components/NavigationBar';
import Home from './components/Home';
import Marketplace from './components/Marketplace';
import Discover from './components/Discover';
import Search from './components/Search';
import Signup from './components/Signup';
import Login from './components/Login';
import './App.css';

function App() {
  const [isSignup, setIsSignup] = useState(true);

  const switchToSignup = () => {
    setIsSignup(true);
  };

  const switchToLogin = () => {
    setIsSignup(false);
  };

  return (
    
      <div className="App">
        <NavigationBar />
        <Routes>
        {/* <Route path="/" exact element={<Signup />} /> */}
          <Route path="/" exact element={isSignup ? <Signup /> : <Login />} />
          {/* <Route path="/home" component={Home} /> */}
          <Route path="/marketplace" component={Marketplace} />
          <Route path="/discover" component={Discover} />
          <Route path="/search" component={Search} />
        </Routes>
      </div>
    
  );
}

export default App;
