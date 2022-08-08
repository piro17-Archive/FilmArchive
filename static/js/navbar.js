const navbarBtn = document.querySelector(".main__navbar-btn img");
const navbarList = document.querySelector(".main__navbar-list");
const body = document.querySelector("body");

navbarBtn.addEventListener("click", function () {
  navbarList.classList.toggle("hidden");
  body.classList.toggle("overlay");
});
