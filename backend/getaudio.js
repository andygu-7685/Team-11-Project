const express = require('express');
const fs = require('fs');
const path = require('path');
const axios = require('axios');
const { spawn } = require('child_process');
const { Server } = require('socket.io');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

app.use('/audio', express.static(path.join(__dirname, 'public', 'audio')));


const dotenv = require('dotenv');
dotenv.config();

console.log(process.env); // Check all environment variables


const AI_TTS_URL = 'https://api.openai.com/v1/audio/speech'; // Example for OpenAI TTS, adjust for your service
const AI_API_KEY = "PUT_YOUR_API_KEY_HERE_DONT DELETE THE QUOTES"; // Store your API key in .env
console.log(AI_API_KEY);
// Your existing code for socket.io and other services...
app.use(express.json());
app.use('/audio', express.static(path.join(__dirname, 'public', 'audio')));  // Serve audio files statically
app.use(cors());  // Allow all domains

// Ensure the directory exists for audio files
const audioDir = path.join(__dirname, 'public', 'audio');
if (!fs.existsSync(audioDir)) {
  fs.mkdirSync(audioDir, { recursive: true });
}


let counter=0;


// Route to generate audio
app.post('/generate-audio', async (req, res) => {
  const { ai_analysis } = req.body;
  if (!ai_analysis) {
    return res.status(400).json({ error: 'No AI analysis text provided' });
  }

  try {
    const response = await axios.post(AI_TTS_URL, {
      model: 'gpt-4o-mini-tts',
      voice: 'coral',
      input: ai_analysis,
      instructions: 'Speak in a demonic and negative tone.'
    }, {
      headers: {
        'Authorization': `Bearer ${AI_API_KEY}`,
        'Content-Type': 'application/json'
      },
      responseType: 'arraybuffer', // Receive audio data
    });

    // Save the audio file (WAV format) in a directory
    const audioPath = path.join(__dirname, 'public', 'audio', 'generated_audio'+counter+'.wav');
    fs.writeFileSync(audioPath, Buffer.from(response.data));
    console.log(`Audio file saved to ${audioPath}`);

    // Send back the audio file URL
    const audioUrl = `http://localhost:8001/audio/generated_audio`+counter+`.wav`; 
    counter = counter + 1;
    res.json({ success: true, audioUrl });

  } catch (error) {
    console.error('Error generating audio:', error);
    res.status(500).json({ error: 'Failed to generate audio' });
  }
});

app.listen(8001, () => {
  console.log('Backend running on port 8001');
});