document.addEventListener('DOMContentLoaded', function () {
    let audio = document.getElementById('background-audio');
    let playButton = document.getElementById('play-button');
    let stopButton = document.getElementById('stop-button');
    let resetButton = document.getElementById('reset-button');
    playButton.addEventListener('click', function () {
      audio.play();
    });
    stopButton.addEventListener('click', function () {
      audio.pause();
    });
    resetButton.addEventListener('click', function() {
        audio.currentTime = 0;
        audio.play();
    });
});
