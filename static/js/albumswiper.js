const swiper = new Swiper('.swiper', {
  slidesPerView: 1, //레이아웃 뷰 개수

  // Optional parameters
  direction: 'horizontal', 
  loop: true,

  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});