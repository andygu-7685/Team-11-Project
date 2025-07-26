import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');

function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [temperature, setTemperature] = useState(null);
  const [humidity, setHumidity] = useState(null);
  const [distance, setDistance] = useState(null);
  const [textInput, setTextInput] = useState(""); // <-- New text input state

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
      setHumidity(parseFloat(data));
    });

    return () => {
      socket.off('picture_taken');
      socket.off('ultrasonic');
      socket.off('temp');
      socket.off('humidity');
      socket.off('light');
    };
  }, []);



  const handleSend = () => {
    if (textInput.trim()) {
      socket.emit("user_input", textInput); // emit your event to server
      setTextInput(""); // clear input box
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
    </div>
  );
}

export default App;
