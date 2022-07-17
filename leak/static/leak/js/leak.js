


$('.remove-leak-from-archive').click(function(e){
    e.preventDefault();

        const objectBx = $(this);

        $.ajax({
            type: 'GET',
            url: $(this).data('href'),
            data:{},
            success : function(response){
                objectBx.remove();
            },
            error : function(response){
                alert('action failed silently!')
            },
        });
});



$('.add-leak-to-archive').click(function(e){
    e.preventDefault();
    const objectBx = $(this);
    $.ajax({
        type: 'GET',
        url: $(this).data('href'),
        data:{},
        success : function(response){
            objectBx.remove();
        },
        error : function(response){
            alert('action failed silently!')
        },
    });
});



$('.upvote-leak').click(function(e){
    e.preventDefault();
    const objectBx = $(this);
    const container = objectBx.parent();
    $.ajax({
        type: 'GET',
        url: $(this).attr('href'),
        data:{},
        success : function(response){

            objectBx.remove();
            container.text('↑');
            container.next().text('↓');

        },
        error : function(response){
            alert('action failed silently!\nPerhaps, you are not logged in!')
        },
    });
});


$('.downvote-leak').click(function(e){
    e.preventDefault();
    const objectBx = $(this);
    const container = objectBx.parent();
    $.ajax({
        type: 'GET',
        url: $(this).attr('href'),
        data:{},
        success : function(response){
            alert(response)
            objectBx.remove();
            container.text('↓');
            
            container.prev().text('↑');

        },
        error : function(response){
            alert('action failed silently!\nPerhaps, you are not logged in!')
        },
    });
});

console.log(document.getElementById('social'))
' .linkedin-this .tweet-this .mail-this .reddit-this .telegram-this .whatsapp-this .pinterest-this'
$('.facebook-this').click(function(e){
    e.preventDefault();
    const obj = $(this);
    $.ajax({
        type: 'GET',
        // url: '/leak-add-share-count/' + obj.parent().data('leak_id'),
        url: obj.parent().data('share_url'),
        data:{},
        success : function(response){
        },
        error : function(response){
        },
    });
})






