// Latest properties slide
// Latest-properties
// hamburger menu
var displaysearchmenumobile;
var hm = document.querySelector(".ham-container");
var menu2 = document.querySelector(".list");
var t1 = document.querySelector(".t1");
var t2 = document.querySelector(".t2");
var t3 = document.querySelector(".t3");
$(".ham-container").click(function (e) { 
    e.preventDefault();    
    $(".navigation_menu").toggleClass("navigato");  
    $(".t1").toggleClass("t1-mobile");
    $(".t2").toggleClass("t2-mobile");
    $(".t3").toggleClass("t3-mobile");
    $(".hm-menu").toggleClass("hm-menu-mobile");
});
$(".property-image").hover(function () {
        // over
        $(".end-card").toggleClass("end-card-over");
    }, function () {
        // out
        $(".end-card").removeClass("end-card-over");
    }
);
var down = $(".drop-down").css("display");
$(".list5").hover(function(display12){
    down = display12;
    if( down == "none") {
        $(".drop-down").removeClass("drop-down").addClass("drop-down-display")
    }
})