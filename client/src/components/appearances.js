import { useState } from 'react';

export default function AppearanceForm() {
  const [formData, setFormData] = useState({
    rating: '',
    guest_id: '',
    episode_id: ''
  });

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch('http://localhost:5555/appearances', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        rating: parseFloat(formData.rating),
        guest_id: parseInt(formData.guest_id),
        episode_id: parseInt(formData.episode_id)
      })
    })
    .then(res => res.json())
    .then(data => {
      console.log('Posted:', data);
      alert("Appearance added successfully!");
    })
    .catch(err => {
      console.error("Error posting:", err);
      alert("Failed to add appearance.");
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Appearance</h2>
      
      <label>Rating (0–5):</label><br />
      <input type="number" step="0.1" name="rating" value={formData.rating} onChange={handleChange} /><br />

      <label>Guest ID:</label><br />
      <input type="number" name="guest_id" value={formData.guest_id} onChange={handleChange} /><br />

      <label>Episode ID:</label><br />
      <input type="number" name="episode_id" value={formData.episode_id} onChange={handleChange} /><br />

      <button type="submit">Submit</button>
    </form>
  );
}
