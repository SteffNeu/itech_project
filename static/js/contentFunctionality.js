
$(document).ready(function(){
    var currentEdit = "no_comment"
    var user_stauts = document.getElementById("user_authentication").innerHTML
    var user_authenticated = (user_stauts == 'true')


    $('.report').click( function(source){


        var input = source.target.id
        var split = input.split("_")
        var id = split[0]
        var flag = split[1]

        var wasPressed =  document.getElementById(input).disabled
        if(!wasPressed){
                var r = confirm("Do you want to report this content?");
                if (r == true) {
                    alert("The content was reported")
                } else {
                    return
                }

            var data = {
                id:id,
                flag: flag,
            }

            $.ajax({
                type: "POST",
                url: "report/",
                data: data,
                success: function(responseData) {
                },
                error: function(){
                    alert("something went wrong with reporting the content")
                    }
            });
            document.getElementById(input).disabled = true;
        }
        else{
            alert("Content is already reported!")
        }
    });


    $('.edit').click( function(source){

        if (currentEdit == "no_comment"){
            var input = source.target.id
            var split = input.split("_")
            var comment_id = split[0]
            var reference = "#"+comment_id+"_comment"

            currentEdit = reference

            var data = $(reference)
            data.attr("contentEditable","true")
            data.css({"border-color": "#C1E0FF",
                 "border-width":"2px",
                 "border-style":"solid"});

            var buttonID = comment_id+"_submit_change"
            document.getElementById(buttonID).style.visibility = "visible"
        }
    });

    $('.submit_change').click(function (source) {
        var input = source.target.id
        var split = input.split("_")
        var comment_id = split[0]
        var buttonID = comment_id+"_submit_change"
        var data = $(currentEdit)

        var url = source.target.getAttribute('data-url')

        data.attr("contentEditable","false")
        data.css({"border-style":"none"});
        currentEdit = "no_comment"
        document.getElementById(buttonID).style.visibility = "hidden"
        var n_comment= data["0"].innerText

        var info = {
                comment_id:comment_id,
                comment_content:n_comment,
        }

        $.ajax({
            type: "POST",
            url: url,
            data: info,
            success: function(responseData) {
            },
            error: function(){
                alert("something went wrong with updating the comment")
            }
        });
    })




    $('.r_icon').click(function (source) {
        if(!user_authenticated){
            return
        }
            <!--get toggle status-->
        var toggled = source.target.getAttribute("aria-pressed")
        var id = source.target.id;

        var split = id.split("_")
        var post_id = split[0]
        var feat = split[1]

        var count_id = id+"_count";
        var count = document.getElementById(count_id).innerHTML;
        if(toggled === "true"){
           count--;
           source.target.setAttribute("aria-pressed",false);
        }
        else{
            count++;
           source.target.setAttribute("aria-pressed",true);
        }
        document.getElementById(count_id).innerHTML = count;

            var data = {
            post_id:post_id,
            feat:feat,
            value: count,
        }

            $.ajax({
                    type: "POST",
                    url: "update_post_feat/",
                    data: data,
                    success: function(responseData) {
                    },
                    error: function(){
                        alert("something went wrong with updating post ratings")
                    }
                });

    })

    $('.c_icon').click( function(source){
        if(!user_authenticated){
            return
        }

        <!--get toggle status-->
        var toggled = source.target.getAttribute("aria-pressed")
        var id = source.target.id;

        var split = id.split("_")
        var comment_id = split[0]
        var feat = split[1]

        var count_id = id+"_count";
        var count = document.getElementById(count_id).innerHTML;
        if(toggled === "true"){
           count--;
           source.target.setAttribute("aria-pressed",false);
        }
        else{
            count++;
           source.target.setAttribute("aria-pressed",true);
        }
        document.getElementById(count_id).innerHTML = count;

            var data = {
            comment_id:comment_id,
            feat:feat,
            value: count,
        }

        $.ajax({
                    type: "POST",
                    url: "update_comment_feat/",
                    data: data,
                    success: function(responseData) {
                    },
                    error: function(){
                        alert("something went wrong with updating comment rating")
                    }
                });


    })

    $(".commentForm").submit(function(event) {
        event.preventDefault()
        var source = event.target
        var post_id = source.getAttribute('data-postID')
        var user = source.getAttribute('data-user')
        var url = source.getAttribute('data-url')
        var comment = document.getElementById(post_id+'_content').value

        //after submitting the statement empty the textfield
        document.getElementById(post_id+'_content').value = ""

        var data = {
            user:user,
            post_id:post_id,
            comment:comment,
        }

        $.ajax({
                    type: "POST",
                    url: url,
                    data: data,
                    success: function(responseData) {
                    },
                    error: function(){
                        alert("something went wrong with submitting the comment")
                    }
                });
    });
});