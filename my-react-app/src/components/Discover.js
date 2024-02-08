// Discover.js
import React, { useEffect, useState } from 'react';

const Discover = () => {
  const [games, setGames] = useState([]);

  useEffect(() => {
    // Fetch game data from an API
    // This is a placeholder for your actual API call
    const fetchGames = async () => {
      try {
        const response = await fetch('https://api.example.com/games');
        const data = await response.json();
        setGames(data);
      } catch (error) {
        console.error('Error fetching games:', error);
      }
    };

    fetchGames();
  }, []);

  const freeGames = games.filter(game => game.isFree);
  const paidGames = games.filter(game => !game.isFree);

  return (
    <div className="page">
      <h2>Discover</h2>
      <h3>Free Games</h3>
      <ul>
        {freeGames.map(game => (
          <li key={game.id}>{game.name}</li>
        ))}
      </ul>
      <h3>Paid Games</h3>
      <ul>
        {paidGames.map(game => (
          <li key={game.id}>{game.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Discover;
