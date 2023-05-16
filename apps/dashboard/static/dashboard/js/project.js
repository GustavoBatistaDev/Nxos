
const link = document.querySelector('#delete');

link.addEventListener('click', function(event) {
  event.preventDefault(); // previne o redirecionamento para a página definida no atributo "href"
  const href = this.getAttribute("href");
  let buttonConfirm = document.querySelector('#confirm').addEventListener('click', (e)=>{
   
    window.location.href = href;
  })
});