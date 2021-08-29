function get_percent() {
            $.ajax({
                type: "POST",
                url: "/get_percent",
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    var json = jQuery.parseJSON(response)
                    $('#percent').html(json.percent);
                    $('#myMoney').html(json.myMoney)
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }