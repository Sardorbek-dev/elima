$(window).load(function() {
    $('.flexslider').flexslider({
        animation: "slide",
        animationLoop: false,
        itemWidth: 650,
        itemMargin: 25,
        minItems: 1,
        maxItems: 3
    });

    $('.flexslider-news-details').flexslider({
        animation: "slide",
        animationLoop: false,
        itemWidth: 350,
        itemMargin: 25,
        minItems: 1,
        maxItems: 3
    });
});
