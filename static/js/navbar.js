const navbar = document.querySelector(".main__navbar");
const navbarBtn = document.querySelector(".main__navbar-btn img");
const navbarList = document.querySelector(".main__navbar-list");
const background = document.querySelector(".darkly");

navbarBtn.addEventListener("click", function () {
  navbarList.classList.toggle("hidden");
  background.classList.toggle("overlay");
  navbar.classList.toggle("navbar-background");
});

const navbarHeight = navbar.getBoundingClientRect().height;

window.addEventListener("scroll", () => {
  if(window.scrollY > navbarHeight) {
    navbar.classList.add("navbar-background-list");
  }else {
    navbar.classList.remove("navbar-background-list");
  }
})