'use-strict'
const Timidity = require('timidity')
let player
let currentlyPlaying = null

class MidiPlayer {
  constructor () {
    this.player = new Timidity('assets/timidity')
    this.player.on('playing', () => {
      console.log('currently playing', currentlyPlaying)
      console.log(player) // => 351.521
    })
    this.playButton = document.querySelector('.play-button')
    this.playButton?.addEventListener('click', this.play.bind(this))
    this.stopButton = document.querySelector('.stop-button')
    this.stopButton?.addEventListener('click', this.pause.bind(this))
    this.statusEl = document.querySelector('.status')
    this.setStatus('Click any .mid file above to play!')
    // this.title = null;
  }

  load (url) {
    this.player.load(url)
  }

  play () {
    this.player.play()
    // this.showPause();
  }

  pause () {
    this.player.pause()
    // this.showPlay();
  }

  setStatus (text) {
    this.statusEl.innerHTML = text
  }
}

// add hover functionality to midi files
window.onload = function () {
  player = new MidiPlayer()
  const midiFiles = document.querySelectorAll('.midi-archive-collection-item-surface')
  midiFiles.forEach(function (midiFile) {
    midiFile.addEventListener('click', handlePlay)
    // midiFile.addEventListener('mouseout', handlePlay);
  })
}

function handlePlay (event) {
  const { target } = event // .midi-archive-collection-item-surface
  const collectionItem = target.parentNode
  const a = collectionItem.querySelector('a')

  if (!a) {
    console.error('MIDI element not found:', a)
  }
  const href = a.getAttribute('href')

  if (href === currentlyPlaying?.getAttribute('href')) return

  player.load(href)
  player.play()

  // add class to visually signify that the file is playing
  if (currentlyPlaying) {
    currentlyPlaying.classList.toggle('playing') // turn off previous
  }
  collectionItem.classList.toggle('playing') // turn on current
  currentlyPlaying = collectionItem

  const filename = href.split('/').pop()
  player.setStatus(`now playing  <strong>${filename}</strong>`)
}
