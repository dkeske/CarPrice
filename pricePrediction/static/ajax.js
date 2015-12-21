$(document).ready(function(){
    $('#myModal').modal({ show: false});

    $('#calculate').click(function(){

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        var kw = $('#kw').val();
        var km = $('#km').val();
        var year = $('#year').val();
        var ac = $('#ac').val();
        var gears = $('#gears').val();
        var bodyType = $('#bodyType').val();
        if(kw==="" || km==="" || year===""){
            $('#errorMessage').text("Please fulfill all the fields!");
        }else {
            $('#errorMessage').text(" ");
            $('#myModal').modal('show');
            var data = {
                kw : kw,
                km : km,
                year: year,
                ac : ac,
                gears : gears,
                body : bodyType
            };
            $.post("/", data, function(priceData){
                $('#calculatedPrice').append(priceData.price);
            });
        }

    });
    $('#userSubmit').click(function(){
        var userPrice = $('#userPrice').val();
        var kw = $('#kw').val();
        var km = $('#km').val();
        var year = $('#year').val();
        var ac = $('#ac').val();
        var gears = $('#gears').val();
        var bodyType = $('#bodyType').val();
        var data = {
            kw : kw,
            km : km,
            year: year,
            ac : ac,
            gears : gears,
            body : bodyType,
            userPrice : userPrice
        };
        $.post("/userSubmit", data, function(){
            $('#errorMessage').text("Danke! <3");
        });
    });
});