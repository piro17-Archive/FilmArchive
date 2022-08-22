new Swiper('.swiper1', {
  slidesPerView: 1, //레이아웃 뷰 개수

  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },

  // Optional parameters
  direction: 'horizontal', 
  loop: true,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    clickable : true,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});