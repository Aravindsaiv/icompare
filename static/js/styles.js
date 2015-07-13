$(function() {
  $("#mycanvas1").on("change", function() {
    $("#im_field1").prop("src", $(this).val());
  });
});

$(function() {
  $("#mycanvas2").on("change", function() {
    $("#im_field2").prop("src", $(this).val());
  });
});

document.getElementById('url_btn1').onclick = function() {
            var val = document.getElementById('mycanvas1').value,
 	              img = document.getElementById('im_field1');

            img.src = val;
            document.body.appendChild(img);
        }
	// $("#im_field2").prop("src", $link);
}

$('#url_btn1').on('click', function() {
    var img = $('<img  height="300" width="350"/>', {src : $('#mycanvas1').val()});
    img.appendTo('#append1');
});