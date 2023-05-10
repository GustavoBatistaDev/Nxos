// Chave de API do OpenAI
const apiKey = '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'
$("#messageArea").on("submit", function(e){
    e.preventDefault();

    const date = new Date();
					const hour = date.getHours();
					const minute = date.getMinutes();
					const str_time = hour+":"+minute;
					var rawText = $("#message-input").val();
					
					$("#message-input").val("");
                    var userHtml = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' + rawText + '<span class="msg_time_send">'+ str_time + 
                    '</span></div><div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div></div>';
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
                       
                        var botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' + response.choices[0]['text'] + '<span class="msg_time">' + str_time + '</span></div></div>';
						$("#messageFormeight").append($.parseHTML(botHtml));
                      
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