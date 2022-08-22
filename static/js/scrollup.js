const topBtn = document.querySelectorAll(".scrollup");

topBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
});