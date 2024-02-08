// Home.js
import React, { useEffect, useState } from 'react';
import Game from './Game';


const Home = () => {
  const [games, setGames] = useState([])

  useEffect(() => 
  fetch('http://127.0.0.1:5554/games')
    .then(response => response.json())
    .then(data => setGames(data))
   ,[])

console.log("updated games")
console.log(games)

const displapGame = games.map(game => (<Game key={game.id} gameData={game} />));
  return (
    <div className="page">
      <h2>Home Page</h2>
      {/* Display list of free games */}
      {displapGame}
    </div>
  );
};

export default Home;
