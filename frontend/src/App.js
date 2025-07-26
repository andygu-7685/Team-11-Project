import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');

function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [temperature, setTemperature] = useState(null);
  const [humidity, setHumidity] = useState(null);

  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });

  
    socket.on('temp', data => {
      setTemperature(data.temperature);
    });

    socket.on('humidity', data => {
      setTemperature(data.temperature);
    });

    return () => {
      socket.off('picture_taken');
      socket.off('temp');
      socket.off('humidity');
    };
  }, []);

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
          <h2>Temperature</h2>
          <p>{temperature !== null ? `${temperature} °C` : "Waiting..."}</p>
        </div>

        <div className="data-block">
          <h2>Humidity</h2>
          <p>{humidity !== null ? `${humidity} %` : "Waiting..."}</p>
        </div>
      </div>
    </div>
  );
}

export default App;
