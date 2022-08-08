const navbarBtn = document.querySelector(".main__navbar-btn img");
const navbarList = document.querySelector(".main__navbar-list");
const background = document.querySelector("main");

navbarBtn.addEventListener("click", function () {
  navbarList.classList.toggle("hidden");
  background.classList.toggle("overlay");
});
