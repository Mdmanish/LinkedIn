$(document).on("submit", "#post-form", function (e) {
  e.preventDefault();

  $.ajax({
    type: "POST",
    url: "/send",
    data: {
      reciver: $("#reciver").val(),
      message_obj_id: $("#message_obj_id").val(),
      message: $("#message").val(),
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
    },
    success: function (data) {
      // alert(data);
    },
  });
  document.getElementById("message").value = "";
});



$(document).ready(function () {
  setInterval(function () {
    reciver= $("#reciver").val();
    $.ajax({
      type: "GET",
      url: "/all_messages/"+reciver,
      success: function (response) {
        console.log(response);
        $("#display-sender").empty();
        $("#display-reciver").empty();
        for (var key =0; key< response.all_message.length;key++) {
          if(response.all_message[key].sender_id == response.sender_id){
            var temp = "<div class='container sender'><b>" + response.sender_user + "</b><p>" + response.all_message[key].value + "</p></div>";
            $("#display-sender").append(temp);
          }
          else{
            var temp1 = "<div class='container reciver'><b>" + response.reciver_user + "</b><p>" + response.all_message[key].value + "</p></div>";
            $("#display-sender").append(temp1);
          }
          // console.log(response.all_message[key].reciver)
        }
        console.log(response.all_message)
      },
      error: function (response) {
        // alert('An error occured')
      }
    });
  }, 1000);
})



document.getElementById("display-sender").classList.add("container");
document.getElementById("display-sender").classList.add("sender");
document.getElementById("display-reciver").classList.add("container");
document.getElementById("display-reciver").classList.add("reciver");

var data =JSON.parse(json_result);

console.log(data)

document.querySelector("sender"+data.sender_user).style.textAlign = "right";