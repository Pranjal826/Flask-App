import React, { useState, useEffect } from 'react';
import 'video.js';
import 'video.js/dist/video-js.css';
import './App.css'
function App() {
  const [overlayText, setOverlayText] = useState('');
  const [rtspUrl, setRtspUrl] = useState('');
  const [overlaySettings, setOverlaySettings] = useState({});
  const [isPlaying, setPlaying] = useState(true);
  const [volume, setVolume] = useState(0.5);
  const [player, setPlayer] = useState(null);

  useEffect(() => {
    fetchOverlaySettings();
  }, []);

  useEffect(() => {
    initializeVideoPlayer();

    // Clean up when the component unmounts
    return () => {
      if (player) {
        player.dispose();
      }
    };
  }, [rtspUrl, overlayText]);

  const initializeVideoPlayer = () => {
    const options = {
      controls: true,
      autoplay: true,
      fluid: true,
      sources: [{ src: rtspUrl, type: 'application/x-rtsp' }],
    };
      const vjsPlayer = videojs('video-player', options);
  
    vjsPlayer.ready(() => {
      vjsPlayer.overlay({
        content: overlayText,
        start: 'playing',
        end: 'paused',
      });
  
      setPlayer(vjsPlayer);
    });
  };
  const fetchOverlaySettings = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/overlay');
      
      const data = await response.json();
      setOverlaySettings(data);
    } catch (error) {
      console.error('Error fetching overlay settings:', error);
    }
  };


  const createOverlay = async () => {
    try {
      await fetch('http://127.0.0.1:5000/api/overlay', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: overlayText }),
      });
      fetchOverlaySettings();
    } catch (error) {
      console.error('Error creating overlay:', error);
    }
  };

  const updateOverlay = async () => {
    try {
      await fetch('http://127.0.0.1:5000/api/overlay', {
        method: 'POST',  // Assuming your API updates using POST, adjust this as needed
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: overlayText }),
      });
      fetchOverlaySettings();
    } catch (error) {
      console.error('Error updating overlay:', error);
    }
  };

  const deleteOverlay = async () => {
    try {
      await fetch('http://127.0.0.1:5000/api/overlay', {
        method: 'DELETE',
      });
      fetchOverlaySettings();
    } catch (error) {
      console.error('Error deleting overlay:', error);
    }
  };

  return (
    <div className="App">
      <div>
        <h1>RTSP Video Streaming App</h1>
        <label>RTSP URL:</label>
        <input
          type="text"
          value={rtspUrl}
          onChange={(e) => setRtspUrl(e.target.value)}
        />
      </div>
      <div className='video-overlay'>
        <h2>Video Overlay</h2>
        <input
          type="text"
          value={overlayText}
          onChange={(e) => setOverlayText(e.target.value)}
        />
        <button onClick={createOverlay}>Create Overlay</button>
        <button onClick={updateOverlay}>Update Overlay</button>
        <button onClick={deleteOverlay}>Delete Overlay</button>
      </div>
      <div>
        <h2>Overlay Settings</h2>
        <pre>{JSON.stringify(overlaySettings, null, 2)}</pre>
      </div>
      <div>
        <h2>Video Controls</h2>
        <div data-vjs-player>
          <video id="video-player" className="video-js vjs-default-skin"></video>
        </div>
        <div>
          <button onClick={() => setPlaying(!isPlaying)}>
            {isPlaying ? 'Pause' : 'Play'}
          </button>
          <label>Volume:</label>
          <input
            type="range"
            min={0}
            max={1}
            step={0.01}
            value={volume}
            onChange={(e) => setVolume(parseFloat(e.target.value))}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
