
$('#delete-leak-draft').click(function(e){
    console.log('working')
    e.preventDefault();
    const objectBx = $(this);
    $.ajax({
        type: 'GET',
        url: $(this).attr('href'),
        data:{},
        success : function(response){
            objectBx.parent().remove();
            document.write('This draft has been deleted') //translate this text back to trans
        },
        error : function(response){
            alert('action failed silently!')
        },
    });
});