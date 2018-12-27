window.onload = function() {

    $('#add_comment_btn').click(function(){

        pk = window.location.pathname.split('/')[2]
        comment = $('#comment').val()
        $.ajax({
            url: "/add_comment/",
            type: "POST",
            data: {
                pk: pk,
                comment: comment,
            },
            success: function(response) {
                console.log("Success!", response);
                var div = document.getElementById('new_comment');
                div.innerHTML += response['comment'] + '<br>';
            },
            error: function(xhr, textstatus, errorthrown) {
                console.log("Please report this error: "+errorthrown+xhr.status+xhr.responseText);
            }
        });
    });

    $('#upvote_btn').click(function(){
        pk = window.location.pathname.split('/')[2]
        $.ajax({
            url: "/upvote/",
            type: "POST",
            data: {
                pk: pk
            },
            success: function(response) {
                console.log("Success!", response);
                var div = document.getElementById('just_upvoted').innerHTML = response['votes']
            },
            error: function(xhr, textstatus, errorthrown) {
                console.log("Please report this error: "+errorthrown+xhr.status+xhr.responseText);
            }
        });
    });
}