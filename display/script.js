// var h4Element = document.createElement("h4");
// h4Element.textContent = "Your Heading Text"; // Change this text to your desired heading

// h4Element.classList.add("mainsub");

// var mainSubDiv = document.querySelector(".mainsubdiv");

// mainSubDiv.appendChild(h4Element);


var userbacking = document.createElement("div")
userbacking.classList.add("userbacking")
var userimagecontainer = document.createElement("div")
userimagecontainer.classList.add("userimagecontainer")
var userimage = document.createElement("img")
userimage.src = "userimage.png"
userimagecontainer.appendChild(userimage)
userbacking.appendChild(userimagecontainer)
var userstatuscontainer = document.createElement("div")
userstatuscontainer.classList.add("userstatuscontainer")
userbacking.appendChild(userstatuscontainer)



var backing = document.querySelector(".backing")
backing.appendChild(userbacking)
