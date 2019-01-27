$(document).ready(function(){

  $("#trash").click(function(){
    boardId = $("#trashId").val()
    value = $("#trashValue").val()
    $.post("test", '{"deviceType": "trash", "boardId": "' + boardId + '", "data": " /d/d ' + value + ' kg"}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });

  $("#water").click(function(){
    boardId = $("#waterId").val()
    value = $("#waterValue").val()
    $.post("test", '{"deviceType": "water", "boardId": "' + boardId + '", "data": "  ' + value + ' L"}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });

  $("#electricity").click(function(){
    boardId = $("#electricityId").val()
    value = $("#electricityValue").val()
    $.post("test", '{"deviceType": "electricity", "boardId": "' + boardId + '", "data": {"value": ' + value + ', "unit": "kWh"}}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });

  $("#gas").click(function(){
    boardId = $("#gasId").val()
    value = $("#gasValue").val()
    $.post("test", '{"deviceType": "gas", "boardId": "' + boardId + '", "value": ' + value + ', "unit": "MJ"}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });

});
