$(function() {
    var div = $('#try-it-btn');
    var width = div.width();
    
    div.css('height', width);
});

window.fadeIn = function(obj) {
    $(obj).fadeIn(1000);
}
$("#preload").load(function(evt){
    $(this).fadeIn(1000);
});