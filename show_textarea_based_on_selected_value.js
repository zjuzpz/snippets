$("#txtarea").hide();

$( "#slct" ).change(function() {
   var val = $("#slct").val();
if(val=="Other"){
    $("#txtarea").show();
} else {
    $("#txtarea").hide();
}
});
