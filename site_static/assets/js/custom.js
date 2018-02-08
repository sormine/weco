
$(document).ready(function() {	

	if (!$('body').hasClass('selected')) {
		alert;
	}

	// SIDR
	$(document).ready(function() {
	  $('#mainmenu').sidr({
		displace: false,
		onClose: function(){
			$("#mainmenu").removeClass("burger-close");
			$("#overlay").removeClass("show");
		},
		onOpen: function(){
			$("#overlay").addClass("show");
		}
	  });
	});

	$('#overlay').click(function () {
	  $.sidr('close', 'sidr');
	});
	
	$('#mainmenu').click(function() {
		$(this).toggleClass('burger-close');
	});
	
	
	
	// Tooltips Bootstrap	
	$(function () {
	  //$('[data-toggle="tooltip"]').tooltip()
	});
	
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

});


/* Loading Home */
$(document).ready(function() {
	
	setTimeout(function(){
		$('body').addClass('loaded');
		$('h1').css('color','#222222')
	}, 1000);

});


// Hide-Show (Menu products)
$(document).ready(function(){
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
});




