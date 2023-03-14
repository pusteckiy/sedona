var balance = $("#balance")


window.addEventListener('click', filter, false)
function filter(e){
  if (e.target.className === 'buy') {
    e.preventDefault();
    
    var posting = $.post( e.target.href );
    posting.done(function(data) {
        if(data.status == 'ok') {
            $.notify(data.message, 'success');
        } else {
            $.notify(data.message, 'error');
        }
    })
  }
}
