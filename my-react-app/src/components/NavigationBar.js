// NavigationBar.js
import React from 'react';
import { Link } from 'react-router-dom';

const NavigationBar = () => {
  return (
    <nav className="navbar">
      <div className="navbar__brand">ROBUX GAMES</div>
      <div className="navbar__links">
        <Link to="/home">Home</Link>
        <Link to="/marketplace">Marketplace</Link>
        <Link to="/discover">Discover</Link>
        <Link to="/search">Search</Link>
      </div>
    </nav>
  );
};

export default NavigationBar;
