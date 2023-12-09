'use-strict';
const Timidity = require('timidity');
const freepats = require('freepats')

const player = new Timidity('assets/timidity');
player.on('playing', () => {
  console.log(player.duration) // => 351.521
})

const websocketURL = 'wss://1wtfmfef4k.execute-api.us-east-2.amazonaws.com/production/';

function connectAndSendMessage() {
    let socket = new WebSocket(websocketURL);

    socket.onopen = function(e) {
        console.log("[open] Connection established");
        // socket.send("My message");
    };

    socket.onmessage = function(event) {
        console.log(`[message] Data received from server: ${event.data}`);
    };

    socket.onerror = function(error) {
        console.log(`[error] ${error.message}`);
    };

    return socket;
}

function ping() {
    console.log("This function is executed every 10 seconds");
    ws.send("Give me the next note please");
}

// skipping websocket implementation for now
// ws = connectAndSendMessage();
// let intervalId = setTimeout(ping, 10000); // 10000 milliseconds = 10 seconds


// test the following on user interaction
const ac = new AudioContext();
// sfInstrument = await Soundfont.instrument(ac, 'acoustic_grand_piano');

async function playMIDI_timidity(url) {
  console.log('url', url);
  player.load(url)
  player.play()
}

// contemplating rolling a custom MIDI player ...
async function playMIDIBadly(url) {
    // Soundfont.instrument(ac, 'acoustic_grand_piano').then(function(piano) {
  sfInstrument = await Soundfont.instrument(ac, 'acoustic_grand_piano');
  console.log('sfInstrument', sfInstrument);
  midiData = await loadMidiFile(url)
  
  track = midiData.tracks[1];
  // console.log('track', track);
  midiData.tracks.forEach(track => {
    let i = 0;
    track.notes.forEach(note => {
      // console.log('note', note);
      sfInstrument.play(note.midi, ac.currentTime + 0.1 * i).stop(ac.currentTime + 1 + 0.1 * i);
      i++;
    });
  });
}

// add hover functionality to midi files
window.onload = function() {
  const midiFiles = document.querySelectorAll('.midi-archive-collection-item-surface');
  midiFiles.forEach(function(midiFile) {
    midiFile.addEventListener('click', handlePlay);
    midiFile.addEventListener('mouseout', handlePlay);
});
}

// Define the hover function
function handlePlay(event) {
    const { target } = event; // .midi-archive-collection-item-surface
    
    const a = target.parentNode.querySelector('a');

    if (!a) {
        console.error('MIDI element not found:', a)
    }
    const href = a.getAttribute('href');

    playMIDI_timidity(href);
    // playMIDIBadly(href)
}

async function loadMidiFile(filepath) {
    // load a midi file in the browser
    const midi = await Midi.fromUrl(filepath)
    //the file name decoded from the first track
    const name = midi.name
    //get the tracks

    // console.log('midi.tracks', midi.tracks);

    midi.tracks?.forEach(track => {
        //tracks have notes and controlChanges

        //notes are an array
        const notes = track.notes
        notes.forEach(note => {
            // console.log('note', note);
            //note.midi, note.time, note.duration, note.name
        })

        //the control changes are an object
        //the keys are the CC number
        // track.controlChanges[64]
        //they are also aliased to the CC number's common name (if it has one)
        // track.controlChanges.sustain.forEach(cc => {
            // cc.ticks, cc.value, cc.time
        // })

    //the track also has a channel and instrument
    //track.instrument.name
    })

    return midi;
}

async function _playMidiFile(url) {
    // Load and parse the MIDI file
    const response = await fetch(url);
    const arrayBuffer = await response.arrayBuffer();
    const midi = new Midi(arrayBuffer);
  
    // Create a synth and connect it to the master output
    const synth = new Tone.Synth().toDestination();
  
    // Schedule the notes
    midi.tracks[0].notes.forEach(note => {
      synth.triggerAttackRelease(note.name, note.duration, note.time);
    });
  
    // Start the Tone.js context
    await Tone.start();
  }



// read and parse MIDI file on hover, and feed into soundfont instrument
// update lambda to push a slow stream of notes, and have them articulated by a soundfont instrument