import React, { useState, useEffect } from "react";
import {io} from 'socket.io-client';
import './App.css';
import axios from 'axios';

const socket = io('http://localhost:8000');

function App() {
 
  const [pictureStatus, setPictureStatus] = useState("");
  const [analysis, setAnalysis] = useState('AI analysis text here');
  const [temperature, setTemperature] = useState(null);
  const [humidity, setHumidity] = useState(null);
  const [distance, setDistance] = useState(null);
  const [light, setLight] = useState(null);
  const [textInput, setTextInput] = useState(""); // <-- New text input state
  const [audioUrl, setAudioUrl] = useState('');

  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });

    socket.on('ultrasonic', data => {
        setDistance(parseFloat(data));  // assuming data is like "23.456"
    });

    socket.on('temp', data => {
      setTemperature(parseFloat(data));
    });

    socket.on('humidity', data => {
      setHumidity(parseFloat(data));
    });

    socket.on('light', data => {
      setLight(parseFloat(data));
    });

    socket.on('ai_analysis', data => {
      console.log(data);
      setAnalysis(data);
    });

    return () => {
      socket.off('picture_taken');
      socket.off('ultrasonic');
      socket.off('temp');
      socket.off('humidity');
      socket.off('light');
      socket.off('ai_analysis');
    };
  }, []);


// Handle the sending of text input
  const handleSend = () => {
    if (textInput.trim()) {
      socket.emit("user_input", textInput); // emit your event to server
      console.log(textInput);
      setTextInput(""); // clear input box
    }
  };

  const handleGenerateAudio = async () => {
    try {
      const response = await axios.post('http://localhost:8001/generate-audio', {
        ai_analysis: analysis
      });

      if (response.data.success) {
        setAudioUrl(response.data.audioUrl); // Set the audio file URL
        console.log('Audio file generated successfully!');
      } else {
        console.error('Failed to generate audio');
      }
    } catch (error) {
      console.error('Error generating audio:', error);
    }
  };

  return (
  <div className="app">
    <h1>Sensor Dashboard</h1>

    {pictureStatus && (
      <div className="status">
        <strong>{pictureStatus}</strong>
      </div>
    )}

    <div className="sensor-data">
      <div className="data-block">
        <h2>Distance</h2>
        <p>{distance !== null ? `${distance} cm` : "Waiting..."}</p>
      </div>

      <div className="data-block">
        <h2>Temperature</h2>
        <p>{temperature !== null ? `${temperature} °C` : "Waiting..."}</p>
      </div>

      <div className="data-block">
        <h2>Humidity</h2>
        <p>{humidity !== null ? `${humidity} %` : "Waiting..."}</p>
      </div>
    </div>

    {/* Take Picture Button */}
    <button onClick={() => socket.emit('take_picture')}>
      Take Picture 📸
    </button>

    {/* New Text Input Box */}
    <div className="input-box">
      <input
        type="text"
        value={textInput}
        onChange={e => setTextInput(e.target.value)}
        placeholder="Type a command or message"
      />
      <button onClick={handleSend}>Send</button>
    </div>

    <div className="container">
      <div className="image-box">
        <img src="/downloaded_image.jpg" alt="My Image" className="custom-image" />
      </div>

      <div className="response-box">
        <h2>AI analysis</h2>
        <p>{analysis ? `${analysis} ` : "Waiting..."}</p>
      </div>
    </div>

    {/* Button to generate audio */}
      <button onClick={handleGenerateAudio}>Generate Audio</button>

      {/* Display the audio file once generated */}
      {audioUrl && (
        <div>
          <h3>Generated Audio:</h3>
          <audio controls>
            <source src={audioUrl} type="audio/wav" />
            Your browser does not support the audio element.
          </audio>
        </div>
      )}

  </div>
);
}

export default App;

