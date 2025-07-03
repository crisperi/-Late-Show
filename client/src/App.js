import './App.css';
import { useEffect, useState } from 'react';


function App() {
  const [episodes, setEpisodes] = useState([])

  useEffect(() => {
    fetch("http://localhost:5555/episodes")
      .then((res) => {
        if (!res.ok) throw new Error("failes to fetch episodes");
        return res.json()
      })
      .then((data) => setEpisodes(data))
      .catch((err) => console.log(err))



  },
    []
  )


  return (
    <>
      <h1>Episodes</h1>
      <ul>
        {episodes.map((episode) => {
          return <li key={episode.id}>

            #{episode.number} - {new Date(episode.date).toLocaleDateString()}
          </li>
        })}
      </ul>
    </>
  );
}

export default App;
