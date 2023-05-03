$(document).ready(function() {
    $('.input-names').on('input', function() {
      // aqui você pode inserir a lógica de validação dos campos
      // por exemplo:
      if ($(this).val().length < 2) {
        $(this).addClass('is-invalid');
      } else {
        $(this).removeClass('is-invalid');
        $(this).addClass('is-valid');
      }
    });
  });

  
  $(document).ready(function() {
    $('.input-passwords').on('input', function() {
    
    //let regex = /^(?=.*[a-z])(?=.*[A-Z])/;

    if($(this).val().length<8){
      $(this).addClass('is-invalid');

    }else{
      $(this).removeClass('is-invalid');
      $(this).addClass('is-valid');
      
    }   
  });
});

  
$(document).ready(function() {
  $('.email-address').on('input', function() {
  
  //let regex = /^(?=.*[a-z])(?=.*[A-Z])/;

  let email = $(this).val()
  if(!email.includes("@") || !email.includes(".")){
    $(this).addClass('is-invalid');

  }else{
    $(this).removeClass('is-invalid');
    $(this).addClass('is-valid');
    
  }   
});
});


