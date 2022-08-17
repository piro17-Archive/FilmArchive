const navbarBtn = document.querySelector(".main__navbar-btn img");
const navbarList = document.querySelector(".main__navbar-list");
const main = document.querySelectorAll("main");

navbarBtn.addEventListener("click", function () {
  navbarList.classList.toggle("hidden");
  main.forEach((item) => {
    item.classList.toggle("overlay");
  });
});

const navbar = document.querySelector(".main__navbar");
const navbarHeight = navbar.getBoundingClientRect().height;

window.addEventListener("scroll", () => {
  if(window.scrollY > navbarHeight) {
    navbar.setAttribute("style", "background: var(--main); transition: 0.4s;");
  } else {
    navbar.setAttribute("style", "background: transparent; transition: 0.4s;");
  }
})