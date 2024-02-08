// Signup.js
import React, { useState } from 'react';

const Signup = ({ switchToLogin }) => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [birthdate, setBirthdate] = useState('');
  const [password, setPassword] = useState('');
  const [gender, setGender] = useState('');

  const handleSignup = () => {
    // Handle signup logic
    console.log('Signing up...');
  };

  return (
    <div>
      <h2>Sign Up</h2>
      <label>Email:</label>
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <br />
      <label>Username:</label>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      <br />
      <label>Birth Date:</label>
      <input type="date" value={birthdate} onChange={(e) => setBirthdate(e.target.value)} />
      <br />
      <label>Password:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <br />
      <label>Gender (optional):</label>
      <input type="text" value={gender} onChange={(e) => setGender(e.target.value)} />
      <br />
      <button onClick={handleSignup}>Sign Up</button>
      <p>Already have an account? <button onClick={switchToLogin}>Login here</button></p>
    </div>
  );
};

export default Signup;
