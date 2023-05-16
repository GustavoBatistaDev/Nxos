(function(){
  $(document).ready(function() {
    $('.input-names').on('input', function() {
      // aqui você pode inserir a lógica de validação dos campos
      // por exemplo:
      if ($(this).val().length < 3) {
        $(this).addClass('is-invalid');
      } else {
        $(this).removeClass('is-invalid');
        $(this).addClass('is-valid');
      }
    });
  });

  $(document).ready(function() {
    // Seleciona as caixas de senha
    var senha1 = $('#password');
    var senha2 = $('#password-2');
  
    // Função que valida as senhas
    function validarSenha() {
      if (senha1.val() === senha2.val() ) {
        // As senhas são iguais
        senha2.removeClass('is-invalid');
        senha2.addClass('is-valid');
        senha1.addClass('is-valid');
      } else {
        // As senhas são diferentes
        senha2.addClass('is-invalid');
        senha1.addClass('is-valid');
      }
    }
  
    // Adiciona o evento "input" às caixas de senha
    senha1.on('input', validarSenha);
    senha2.on('input', validarSenha);
  });

//|| 

let divClose = $('.close').click(function(){
  let containerMessage = $('.container-message')
  containerMessage.remove();
})
  



})();







  
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


