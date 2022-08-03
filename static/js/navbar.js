const navbarBtn = document.querySelector(".main__navbar-btn img");
const navbarList = document.querySelector(".main__navbar-list");

navbarBtn.addEventListener("click", function () {
  navbarBtn.classList.toggle("hidden");
  navbarList.classList.toggle("hidden");
});
