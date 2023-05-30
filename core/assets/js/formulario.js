$('#displayNone').click(function(e) {
  
    // Resetear, por si acaso has estado jugando con la otra propiedad
    $('#planillaCreada').css('visibility', 'visible');
    
    if( $('#planillaCreada').is(":visible") ) {
      $('#planillaCreada').css('display', 'none'); 
    } else {
      $('#planillaCreada').css('display', 'block');
    }
  });
  
  $('#visibilityHidden').click(function(e) {
    
    // Resetear, por si acaso has estado jugando con la otra propiedad
    $('#planillaCreada').css('display', 'block');
    
    if( $('#planillaCreada').css('visibility') != 'hidden' ) {
      $('#planillaCreada').css('visibility', 'hidden');
    } else {
      $('#planillaCreada').css('visibility', 'visible');
    }
  });