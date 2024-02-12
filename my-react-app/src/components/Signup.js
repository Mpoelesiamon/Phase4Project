import React, { useState } from 'react';

const Signup = ({ switchToLogin }) => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [birthdate, setBirthdate] = useState('');
  const [password, setPassword] = useState('');
  const [gender, setGender] = useState('');

  const handleSignup = () => {
    // Prepare data for signup
    const signupData = {
      email: email,
      username: username,
      birthdate: birthdate,
      password: password,
      gender: gender
    };

    // Send POST request to the server
    fetch('http://127.0.0.1:5554/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(signupData)
    })
    .then(response => {
      if (response.ok) {
        console.log('Signup successful');
        // Handle successful signup, e.g., redirect or display success message
      } else {
        console.error('Signup failed');
        // Handle failed signup, e.g., display error message
      }
    })
    .catch(error => {
      console.error('Error occurred during signup:', error);
      // Handle error, e.g., display error message
    });
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
