// PW KeyConVP
// Keyboard Controls for Video Player
// Tested against 'https://study.physicswallah.live/'
// Coded by: GitHub/FireHead90544 (Rudransh Joshi)
// This project is open source, you are free to modify the code to whatever extent you like just be sure to credit the original author/repository.
// I am not a primary javascript developer, so if you find some bugs/issues/errors/suggestions, please let me know.
// Contributions to the same will be appreciated.

// Usage: Copy all the contents of this file --> Open PW's website --> Press Ctrl + Shift + I --> Go to Console tab --> Paste it there --> Press Enter --> Enjoy your controls using keyboard :)

// Spacebar - Play/Pause
// Left Arrow - Seek Backward 10s
// Right Arrow - Seek Forward 10s

document.onkeyup = function(e) {
    var evt = window.event || e;
    if (evt.keyCode == 37) {
        // Left arrow key - Seek Backward
        document.querySelector('.vjs-seek-button.vjs-skip-backward.vjs-icon-replay.vjs-skip-10.vjs-control.vjs-button').click();
    } else if (evt.keyCode == 39) {
        // Right arrow key - Seek Forward
        document.querySelector('.vjs-seek-button.vjs-skip-forward.vjs-icon-replay.vjs-skip-10.vjs-control.vjs-button').click();
    } else if (evt.keyCode == 32) {
        pause = document.querySelector('.vjs-play-control.vjs-control.vjs-button.vjs-paused');
        play = document.querySelector('.vjs-play-control.vjs-control.vjs-button.vjs-playing');
        if (pause) {
            pause.click()
        } else if (play) {
            play.click()
        }
    }
}
