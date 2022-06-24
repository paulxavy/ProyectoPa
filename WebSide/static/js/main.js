
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var corrector = $('.validate-input input[name="corrector"]');
   


    $('.validate-form').on('submit',function(){
        var check = true;

        if($(corrector).val().trim() == ''){
            showValidate(corrector);
            check=false;
        }


        return check;
    });


    $('.validate-form .input1').each(function(){
        $(this).focus(function(){
           hideValidate(this);
       });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);