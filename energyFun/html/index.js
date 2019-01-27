$(document).ready(function(){

  $("#trash").click(function(){
    $.post("test", '{"deviceType": "trash", "boardId": "1A2B3C", "data": " /d/d 12.32 kg"}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });

  $("#water").click(function(){
    $.post("test", '{"deviceType": "water", "boardId": "7C5A2C", "data": "  5.3400 L"}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });

  $("#electricity").click(function(){
    $.post("test", '{"deviceType": "electricity", "boardId": "8X2A3D", "data": {"value": 8.45657, "unit": "kWh"}}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });

  $("#gas").click(function(){
    $.post("test", '{"deviceType": "gas", "boardId": "8A6D5F", "value": 118.00045657, "unit": "MJ"}',
    function(data, status){
      console.log("data: " + data)
      console.log("typeof: " + typeof data)
    });
  });
  
});
