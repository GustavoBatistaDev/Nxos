// Chave de API do OpenAI
const apiKey = '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'
$("#messageArea").on("submit", function(e){
    e.preventDefault();

    const date = new Date();
					const hour = date.getHours();
					const minute = date.getMinutes();
					const str_time = hour+":"+minute;
					var rawText = $("#message-input").val();
                    var rawTextInput = $("#message-input")
					
					$("#message-input").val("");
                    var userHtml = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' + rawText + '<span class="msg_time_send">'+ str_time + 
                    '</span></div><div class="img_cont_msg"><img src="https://static.vecteezy.com/system/resources/previews/000/439/863/original/vector-users-icon.jpg" class="rounded-circle user_img_msg"></div></div>';
                    $("#messageFormeight").append(userHtml);
					
                    fetch("https://api.openai.com/v1/completions",{
                        method: 'POST',
                        headers: {
                            Accept: "application/json",
                            "Content-Type": "application/json",
                            Authorization: `Bearer ${apiKey}`,
                        },
                        body: JSON.stringify({
                            model: "text-davinci-003",
                            prompt: rawText,
                            max_tokens: 2048, // tamanho da resposta
                            temperature: 0.5 // criatividade na resposta
                        })
                    })
                    .then((response) => response.json())
                    .then((response) => {
                       
                        var botHtml = '<div id="" class="d-flex justify-content-start mb-4"> <div class="img_cont_msg"><img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer"><i class="fa-solid fa-copy fa-1x"></i>' + response.choices[0]['text']   + '</div></div>';
						$("#messageFormeight").append($.parseHTML(botHtml));

                        $(document).ready(function() {
                            // Adicionar um ID dinâmico a cada div
                            $(".my-div").each(function(index) {
                              $(this).attr("id", "div-" + (index + 1));
                            });
                            
                            // Adicionar um manipulador de evento de clique em cada ícone de cópia
                            $(".fa-copy").click(function() {
                              // Obter o conteúdo da div correspondente
                              var content = $(this).parent().text().trim();
                              
                              // Copiar o conteúdo para a área de transferência
                              navigator.clipboard.writeText(content);
                              
                              // Exibir uma mensagem informando que o conteúdo foi copiado
                              alert('Texto copiado com sucesso!');
                             
                            });
                          });
                      
                    })
                    .catch((e) => {
                        console.log(`Error -> ${e}`)
                        
                    })
                    .finally(() => {
                       
                        rawTextInput.disabled = false
                        rawTextInput.value = ''
                    })
                   
					});					

// <!--
// <div class="">
//     <div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div>
//     <div class="msg_cotainer">Ola  <span class="msg_time"></span></div>
// </div>
// <div class="d-flex justify-content-start mb-4">
 //    <div class="img_cont_msg"><img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img_msg"></div>
 //    <div class="msg_cotainer">Ola, man  <span class="msg_time">  </span></div>
// </div>
 //  --> 