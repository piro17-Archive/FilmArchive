const navbarBtn = document.querySelector(".main__navbar-btn img");
const navbarList = document.querySelector(".main__navbar-list");

navbarBtn.addEventListener("click", function () {
  navbarList.classList.toggle("hidden");
});
