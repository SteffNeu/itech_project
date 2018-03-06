$(document).ready(function() {
    $("#myTabs li a").click(function() {

        $("#myTabs li a").removeClass('current');
        $(this).addClass('current');
        var useThisURL = '';

        //if ($(this).attr("href") == '#t1') {
         //   useThisURL = '/antifu/tabs/firsttab';
        //}


        $.ajax({ url: useThisURL, success: function(html) {
            $("#t1").empty().append(html);
            }
    });
    return false;
    });

    $.ajax({ url: '/antifu/tabs/firsttab', success: function(html) {
            $("#t1").empty().append(html);
    }
    });
});