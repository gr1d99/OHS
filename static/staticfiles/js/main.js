/**
 * Created by root on 8/16/17.
 */
'use strict';
$('#id_login').addClass("form-control");
$('#id_password').addClass("form-control");
$('#id_subscribe_for_sms').removeClass("form-control");
$('#id_username').addClass("form-control");
$('#id_email').addClass("form-control");
$('#id_password1').addClass("form-control");
$('#id_password2').addClass("form-control");
$('#id_oldpassword').addClass("form-control");

(function( $ ) {

    //Function to animate slider captions
	function doAnimations( elems ) {
		//Cache the animationend event in a variable
		var animEndEv = 'webkitAnimationEnd animationend';

		elems.each(function () {
			var $this = $(this),
				$animationType = $this.data('animation');
			$this.addClass($animationType).one(animEndEv, function () {
				$this.removeClass($animationType);
			});
		});
	}

	//Variables on page load
	var $myCarousel = $('#carousel-example-generic'),
		$firstAnimatingElems = $myCarousel.find('.item:first').find("[data-animation ^= 'animated']");

	//Initialize carousel
	$myCarousel.carousel();

	//Animate captions in first slide on page load
	doAnimations($firstAnimatingElems);

	//Pause carousel
	$myCarousel.carousel('pause');


	//Other slides to be animated on carousel slide event
	$myCarousel.on('slide.bs.carousel', function (e) {
		var $animatingElems = $(e.relatedTarget).find("[data-animation ^= 'animated']");
		doAnimations($animatingElems);
	});
    $('#carousel-example-generic').carousel({
        interval:3000,
        pause: "false"
    });

})(jQuery);
