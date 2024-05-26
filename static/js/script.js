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


document.addEventListener("DOMContentLoaded", function() {
  const starsContainer = document.querySelector('.stars');
  const numStars = 500;

  for (let i = 0; i < numStars; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      star.style.top = `${Math.random() * 100}vh`;
      star.style.left = `${Math.random() * 100}vw`;
      star.style.animationDelay = `${Math.random() * 2}s`;
      star.style.animationDuration = `${Math.random() * 2 + 2}s`;
      starsContainer.appendChild(star);
  }
});