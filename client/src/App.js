import './App.css';
import { useState ,useEffect} from 'react';
import Appearance from './components/appearances';

function App() {
  const [episodes, setEpisodes] = useState([]);
  const [episodeId, setEpisodeId] = useState('');
  const [episodeDetails, setEpisodeDetails] = useState(null);

  // Load episodes only once
  useEffect(() => {
    fetch("http://localhost:5555/episodes")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch episodes");
        return res.json();
      })
      .then((data) => setEpisodes(data))
      .catch((err) => console.log(err));
  }, []);

  // On submit, fetch episode details
  function episodeSubmit(e) {
    e.preventDefault();
    if (episodeId > 0) {
      fetch(`http://localhost:5555/episodes/${episodeId}`)
        .then((res) => {
          if (!res.ok) throw new Error("Failed to fetch episode");
          return res.json();
        })
        .then((data) => setEpisodeDetails(data))
        .catch((err) => console.log(err));
        setEpisodeDetails('')
      }
  }

  return (
    <>
      <h1>Episodes</h1>
      <ul>
        {episodes.map((episode) => (
          <li key={episode.id}>
            #{episode.number} - {new Date(episode.date).toLocaleDateString()}
          </li>
        ))}
      </ul>

      <form onSubmit={episodeSubmit}>
        <label>
          Enter an episode id:
          <input
            type="number"
            name="episode_id"
            value={episodeId}
            onChange={(e) => setEpisodeId(e.target.value)}
          />
        </label>
        <button type="submit">Submit</button>
      </form>

      {episodeDetails && (
        <div>
          <h2>Episode Details</h2>
          <p>Episode #{episodeDetails.number}</p>
          <p>Date: {new Date(episodeDetails.date).toLocaleDateString()}</p>
        </div>
      )}

      <h2>Appearances</h2>
      <Appearance />
    </>
  );
}

export default App;
