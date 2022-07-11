// A simple javascript code to enable the copy paste which's been disabled in the website ;-;
// The copy/paste has been disabled in the PW's website for a reason, and that's to prevent spams, but in some cases you needed to copy and paste several things.
// So this will allow you to copy and paste, but please respect and don't abuse the system by spamming things.

// This stops the rest of the event handlers from being executed
var magik = function(e){
  e.stopImmediatePropagation();
  return true;
};

// Override the event listeners
document.addEventListener('copy', magik, true);
document.addEventListener('paste', magik, true);
