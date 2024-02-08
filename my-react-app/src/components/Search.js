// Search.js
import React, { useState } from 'react';

const Search = () => {
  const [query, setQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSearch = () => {
    const games = [
      'Super Mario Bros',
      'The Legend of Zelda',
      'Minecraft',
      'Fortnite',
      'Among Us',
      'Pac-Man',
    ];

    const filteredResults = games.filter(game =>
      game.toLowerCase().includes(query.toLowerCase())
    );

    setSearchResults(filteredResults);
  };

  return (
    <div className="page">
      <h2>Search</h2>
      <input
        type="text"
        value={query}
        onChange={handleInputChange}
        placeholder="Enter search query..."
      />
      <button onClick={handleSearch}>Search</button>
      {/* Display search results */}
      <div>
        {searchResults.length > 0 ? (
          searchResults.map((result, index) => (
            <div key={index}>{result}</div>
          ))
        ) : (
          <p>No results found.</p>
        )}
      </div>
    </div>
  );
};

export default Search;
