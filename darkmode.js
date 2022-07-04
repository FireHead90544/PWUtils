// PW Dark Mode
// Dark Mode for Physics Wallah's website
// Tested against 'https://study.physicswallah.live/'
// Coded by: GitHub/FireHead90544 (Rudransh Joshi)
// This project is open source, you are free to modify the code to whatever extent you like just be sure to credit the original author/repository.
// I am not a primary javascript developer, so if you find some bugs/issues/errors/suggestions, please let me know.
// Contributions to the same will be appreciated.

// Usage: Copy all the contents of this file --> Open PW's website --> Press Ctrl + Shift + I --> Go to Console tab --> Paste it there --> Press Enter --> Enjoy your dark mode :)

var light = true;
var fixed = false;

// This logic handles the changing of theme
function change_theme(){
   if (light){
      document.getElementsByTagName('html')[0].style.filter = 'invert(1) hue-rotate(180deg)'
      light = false
   }
   else{
      document.getElementsByTagName('html')[0].style.filter = 'invert(0) hue-rotate(0deg)'
      light = true   
   }
   fix_containers();
}
// This logic handles the fixing of images and videos becoming inverted
function fix_containers() {
    if (!fixed){
        var imgs = document.getElementsByTagName("img");
        var vids = document.getElementsByTagName("video");
        var pwlogo = document.getElementsByClassName('mouse_pointer')[0]
        for (var i = 0; i < imgs.length; i++) {
           if (imgs[i].style.filter === ""){
               imgs[i].style.filter = "invert(1) hue-rotate(180deg)";
           }else{
               imgs[i].style.filter = "";
           }
        }
        for (var i = 0; i < vids.length; i++) {
           if (vids[i].style.filter === ""){
               vids[i].style.filter = "invert(1) hue-rotate(180deg)";
           }else{
               vids[i].style.filter = "";
           }
        }
        if (pwlogo.style.filter === ""){pwlogo.style.filter="invert(0) hue-rotate(180deg)";}else{pwlogo.style.filter="";}
        fixed = true
    }
    else{
        fixed = false
    }
}

// This crap creates buttons in left sidebar for technically blind people who cannot press keys (just kidding) xD
// Since the website is updated now, these buttons won't work, use keybinds instead, I'll fix them at some point later on
// var themeBtn = document.createElement("button");
// var fixBtn = document.createElement("button");
// var someDiv = document.createElement("div")
// themeBtn.innerHTML = "Change Theme";
// fixBtn.innerHTML = "Fix Images";
// themeBtn.classList.add("button-native")
// fixBtn.classList.add("button-native")
// themeBtn.style.cssText = "background-color: #5a4bda!important; color: #fff!important; flex: 1; margin: 0 4px; border: 1px solid #e6e6e6; border-radius: 25px; padding: 8px 16px; font-size: 14px; font-weight: 700; cursor: pointer; visibility: inherit; white-space: nowrap; text-align: center"
// fixBtn.style.cssText = "background-color: #5a4bda!important; color: #fff!important; flex: 1; margin: 0 4px; border: 1px solid #e6e6e6; border-radius: 25px; padding: 8px 16px; font-size: 14px; font-weight: 700; cursor: pointer; visibility: inherit; white-space: nowrap; text-align: center"
// var body = document.getElementsByTagName("ion-header")[0];
// someDiv.appendChild(themeBtn);
// someDiv.appendChild(fixBtn)
// body.appendChild(someDiv);
// themeBtn.addEventListener("click", change_theme);
// fixBtn.addEventListener("click", fix_containers)

// Shift + Alt + D --> Dark Mode
// Shift + Alt + F --> Fix Images/Videos
document.onkeyup = function (e) {
    var evt = window.event || e;   
    if (evt.keyCode == 68 && evt.altKey && evt.shiftKey) {
        change_theme();
    }
    else if (evt.keyCode == 70 && evt.altKey && evt.shiftKey) {
        fix_containers();
    }
}
