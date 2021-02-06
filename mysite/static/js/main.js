(function ($) {
"use strict";


  $(window).on('scroll',function() {    
   var scroll = $(window).scrollTop();
   if (scroll < 245) {
    $("#header-sticky").removeClass("scroll-header");
   }else{
    $("#header-sticky").addClass("scroll-header");
   }
  });
  
/* meanmenu */
$('.main-menu nav').meanmenu({
	 meanMenuContainer: '.mobile-menu',
	 meanScreenWidth: "991"
 });


/* slider-active */
$('.slider-active').owlCarousel({
    loop:true,
    nav:true,
	navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
    responsive:{
        0:{
            items:1
        },
        767:{
            items:1
        },
        1000:{
            items:1
        }
    }
})
/* counter */
$('.counter').counterUp({
    delay: 10,
    time: 1000
});


/* testimonial-active */
$('.testimonial-active').owlCarousel({
    loop:true,
    nav:false,
	dots:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:3
        }
    }
})

/* work-active */
$('.works-active').owlCarousel({
    loop:true,
    nav:true,
    dots:false,
	navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
    responsive:{
        0:{
            items:1
        },
        767:{
            items:2
        },
        1000:{
            items:3
        }
    }
})





/* image-link */
$('.image-link').magnificPopup({
  type: 'image',
  gallery:{
    enabled:true
  }
});

/* brand-active */
$('.brand-active').owlCarousel({
    loop:true,
    nav:false,
	autoplay:true,
    responsive:{
        0:{
            items:1
        },
        450:{
            items:2
        },
        768:{
            items:3
        },
        1000:{
            items:5
        }
    }
})
/* project-details-active */
$('.project-details-active').owlCarousel({
    loop:true,
    nav:true,
	autoplay:true,
	navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
    responsive:{
        0:{
            items:1
        },
        450:{
            items:1
        },
        768:{
            items:1
        },
        1000:{
            items:1
        }
    }
})
/* blog-thumb-active */
$('.blog-thumb-active').owlCarousel({
    loop:true,
    nav:true,
	autoplay:true,
	navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
    responsive:{
        0:{
            items:1
        },
        450:{
            items:1
        },
        768:{
            items:1
        },
        1000:{
            items:1
        }
    }
})

/* Scroll Up */
$.scrollUp({
	easingType: 'linear',
	scrollSpeed: 900,
	animation: 'fade',
	scrollText: '<i class="fa fa-angle-up"></i>',
});	


/* testimonial-3-active */
$('.testimonial-3-active').owlCarousel({
    loop:true,
    nav:false,
	dots:false,
	autoplay:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})

/* magnificPopup */
$('.video-popup').magnificPopup({
  type: 'iframe'
});



})(jQuery);	