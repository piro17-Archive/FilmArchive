new Swiper('.swiper2', {
  slidesPerView: 1, //레이아웃 뷰 개수

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