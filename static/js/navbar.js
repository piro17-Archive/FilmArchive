const navbarBtn = document.querySelector(".main__navbar-btn img");
const navbarList = document.querySelector(".main__navbar-list");
const background = document.querySelector(".darkly");

navbarBtn.addEventListener("click", function () {
  navbarList.classList.toggle("hidden");
  background.classList.toggle("overlay");
});

const navbar = document.querySelector(".main__navbar");
const navbarHeight = navbar.getBoundingClientRect().height;

window.addEventListener("scroll", () => {
  if(window.scrollY > navbarHeight) {
    navbar.setAttribute("style", "background: var(--main); transition: 0.2s;");
  } else {
    navbar.setAttribute("style", "background: transparent; transition: 0.2s;");
  }
})