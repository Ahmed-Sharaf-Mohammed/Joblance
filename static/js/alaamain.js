$(document).ready(function() {
    let $btns = $(".pictures-area .button-groub button");
    $btns.click(function(e) {
        $(".pictures-area .button-groub button").removeClass("active");
        e.target.classList.add("active");
        let selector = $(e.target).attr("data-filter");
        $(".pictures-area .grid").isotope({
            filter: selector
        });
        return false;
    });

    $(".pictures-area .button-groub #btn1").trigger("click");

    $(".pictures-area .grid .test-popup-link").magnificPopup({
        type: "image",
        gallery: {
            enabled: true
        }
    });
    //owl carousel
    $(".site-main .they-say .owl-carousel").owlCarousel({
        loop: true,
        autoplay: true,
        dots: true,
        responsive: {
            0: {
                items: 1
            },
            544: {
                items: 2
            }
        }
    });

    AOS.init();
});