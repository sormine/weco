/* ========================================================================
 * DOM-based Routing
 * Based on http://goo.gl/EUTi53 by Paul Irish
 *
 * Only fires on body classes that match. If a body class contains a dash,
 * replace the dash with an underscore when adding it to the object below.
 *
 * .noConflict()
 * The routing is enclosed within an anonymous function so that you can
 * always reference jQuery with $, even when in .noConflict() mode.
 * ======================================================================== */

(function($) {

  // Use this variable to set up the common and page specific functions. If you
  // rename this variable, you will also need to rename the namespace below.
  var Sage = {
    // All pages
    'common': {
      init: function() {


        
      },
      finalize: function() {
        
        $('#mainmenu').sidr({
          displace: false,
          onClose: function(){
            $("#overlay").removeClass("show");
            $('#mainmenu').removeClass("burger-close");
          },
          onOpen: function(){
            $("#overlay").addClass("show");
            $('#mainmenu').addClass('burger-close');
          }
        });

        $('#overlay').click(function () {
          $.sidr('close', 'sidr');
        });
        
        // Tooltips Bootstrap 
        $('[data-toggle="tooltip"]').tooltip();
        
        $(window).scroll(function(e){
          $(".slider-tooltip").css("opacity", 1 - $(window).scrollTop() / 250);
        });
        
        if($(window).scrollTop() > 500){ $(this).find(".slider-tooltip").css("opacity","0"); }

        if($(window).width() > 768) {
          
          // Home Sliders
          var widthWanted = 0;
          var widthLi = 0;
          var widthSpan = 0;
          var widthSpacer = 0;
          var widthExtraSpacer = 0;
          var newWidth = 0;
            
          $('body.home aside li').mouseenter(function() {
            //$(this).addClass('active');
            
            widthWanted = 0;
            widthLi = $(this).outerWidth();
            widthSpan = $(this).find('span').outerWidth();
            widthSpacer = 5;
            widthExtraSpacer = 80;
            newWidth = widthLi + widthSpan + widthSpacer + widthExtraSpacer + 'px';
            var svg = $(this).find('svg');
          
            $(this).css('background','#ed1c2a');
            $(this).css('padding-right', newWidth);
            svg.css('fill','#fff');
            svg.css('stroke','#fff');
            
            if($(window).scrollTop() > 500){ $(this).find(".slider-tooltip").css("opacity","1"); }
            
          });
          $('body.home aside li').mouseleave(function() {
            //$(this).removeClass('active');
          
            widthWanted = 0;
            widthLi = 0;
            widthSpan = 0;
            widthSpacer = 0;
            widthExtraSpacer = 0;
            var svg = $(this).find('svg');
            
            $(this).css('background','transparent');
            $(this).css('padding-right', 0);
            svg.css('fill','#8a8a8a');
            svg.css('stroke','#8a8a8a');
            
            if($(window).scrollTop() > 500){ $(this).find(".slider-tooltip").css("opacity","0"); }
          });
          
          $('body.home .b-service-1').mouseover(function() {
            $("#homeSlider figure").removeClass("active");  
            $('#homeSlider figure').addClass('inactive');
            $('#service-1').removeClass('inactive');
            $('#service-1').addClass('active');
            $('.b-service-1 .slider-tooltip').addClass("show-tooltip");
          });
          $('body.home .b-service-1').mouseout(function() {
            $('.b-service-1 .slider-tooltip').removeClass("show-tooltip");
          });
          
          $('body.home .b-service-2').mouseover(function() {
            $("#homeSlider figure").removeClass("active");
            $("#homeSlider figure").addClass("inactive");
            $('#service-2').removeClass('inactive');
            $('#service-2').addClass('active');
            $('.b-service-2 .slider-tooltip').addClass("show-tooltip");
          });
          $('body.home .b-service-2').mouseout(function() {
            $('.b-service-2 .slider-tooltip').removeClass("show-tooltip");
          });
          
          $('body.home .b-service-3').mouseover(function() {
            $("#homeSlider figure").removeClass("active");
            $("#homeSlider figure").addClass("inactive");
            $('#service-3').removeClass('inactive');
            $('#service-3').addClass('active');
            $('.b-service-3 .slider-tooltip').addClass("show-tooltip");
          });
          $('body.home .b-service-3').mouseout(function() {
            $('.b-service-3 .slider-tooltip').removeClass("show-tooltip");
          });
          
          $('body.home .b-service-4').mouseover(function() {
            $("#homeSlider figure").removeClass("active");
            $("#homeSlider figure").addClass("inactive");
            $('#service-4').removeClass('inactive');
            $('#service-4').addClass('active');
            $('.b-service-4 .slider-tooltip').addClass("show-tooltip");
          });
          $('body.home .b-service-4').mouseout(function() {
            $('.b-service-4 .slider-tooltip').removeClass("show-tooltip");
          });
          
          $('body.home .b-service-5').mouseover(function() {
            $("#homeSlider figure").removeClass("active");
            $("#homeSlider figure").addClass("inactive");
            $('#service-5').removeClass('inactive');
            $('#service-5').addClass('active');
            $('.b-service-5 .slider-tooltip').addClass("show-tooltip");
          });
          $('body.home .b-service-5').mouseout(function() {
            $('.b-service-5 .slider-tooltip').removeClass("show-tooltip");
          });
          
          $('body.home .b-service-6').mouseover(function() {
            $("#homeSlider figure").removeClass("active");
            $("#homeSlider figure").addClass("inactive");
            $('#service-6').removeClass('inactive');
            $('#service-6').addClass('active');
            $('.b-service-6 .slider-tooltip').addClass("show-tooltip");
          });
          $('body.home .b-service-6').mouseout(function() {
            $('.b-service-6 .slider-tooltip').removeClass("show-tooltip");
          });
        
        }
          
        setTimeout(function(){
          $('body').addClass('loaded');
          $('h1').css('color','#222222');
        }, 1000);

        // Hide-Show (Menu products)
        $(".cty button").click(function(){
              $(this).next(".ctysub").slideToggle("fast");
          $(this).parent().next('div').find("i").toggleClass("zmdi-chevron-down");
          $(this).parent().next('div').find("i").toggleClass("zmdi-chevron-right");
        });

        $(".cty button.rightIcon").click(function(){
          $(this).parent().prev('div').find(".ctysub").slideToggle("fast");
          $(this).find("i").toggleClass("zmdi-chevron-down");
          $(this).find("i").toggleClass("zmdi-chevron-right");
        });

        $('.newsSlider').slick({
          dots: false,
          infinite: true,
          speed: 300,
          slidesToShow: 1,
          centerMode: false,
          variableWidth: true
        });

      }
    },
    // Home page
    'home': {
      init: function() {
       
      },
      finalize: function() {

        $("#element").introLoader({
          animation: {
            name: 'doubleLoader',
            options: {
              exitFx:'fadeOut',
              ease: "easeInOutCirc",
              style: 'ocean zebra',
              delayBefore: 500,
              exitTime: 300,
              progbarTime: 700,
              progbarDelayAfter: 400,
              preventScroll: true
            }
          }
        });

      }
    },
    // About us page, note the change from about-us to about_us.
    'about_us': {
      init: function() {
        // JavaScript to be fired on the about us page
      }
    }
  };

  // The routing fires all common scripts, followed by the page specific scripts.
  // Add additional events for more control over timing e.g. a finalize event
  var UTIL = {
    fire: function(func, funcname, args) {
      var fire;
      var namespace = Sage;
      funcname = (funcname === undefined) ? 'init' : funcname;
      fire = func !== '';
      fire = fire && namespace[func];
      fire = fire && typeof namespace[func][funcname] === 'function';

      if (fire) {
        namespace[func][funcname](args);
      }
    },
    loadEvents: function() {
      // Fire common init JS
      UTIL.fire('common');

      // Fire page-specific init JS, and then finalize JS
      $.each(document.body.className.replace(/-/g, '_').split(/\s+/), function(i, classnm) {
        UTIL.fire(classnm);
        UTIL.fire(classnm, 'finalize');
      });

      // Fire common finalize JS
      UTIL.fire('common', 'finalize');
    }
  };

  // Load Events
  $(document).ready(UTIL.loadEvents);

})(jQuery); // Fully reference jQuery after this point.
