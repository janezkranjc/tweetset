$( document ).ready(function() {

    $('.btn').button();

    $("button.ts-loading").click(function() {
    var $btn = $(this);
    $btn.button('loading');
    });

    $("a.ts-loading").click(function() {
    var $btn = $(this);
    $btn.button('loading');
    });    

    $("input.ts-loading").click(function() {
    var $btn = $(this);
    $btn.button('loading');
    });    


    $(".tooltip-control").tooltip({'placement':'right'});

});
