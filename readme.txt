# starting paste this form to send mail
1. update the value of to_mail in form

    <form id="contact_form">
        <h4 id="response_block" style="color: green;"></h4>
         <!-- block for api respone --> 
        <div class="form-group">
            <input type="text" id="name" name="name" placeholder="Enter Your Full Name..." class="form-control form-control-sm" required>
        </div>

        <div class="form-group">
            <input type="number" name="contact" id="contact" class="form-control form-control-sm" placeholder="10 Digit Number" required>
        </div>

        <div class="form-group">

            <input type="email" name="email" id="email" class="form-control form-control-sm" placeholder="Email (optional) ">
        </div>

        
        <div class="form-group">
            <textarea name="message" id="message" class="form-control form-control-sm" rows="3" placeholder="Type Your Message" required></textarea>
        </div>
        
        
        <input type="hidden" name="to_mail" id="to_mail" value="writetodhananjay@gmail.com">
        <input type="hidden" name="check" id="check" placeholder="check">
        <div class="spinner-border text-primary text-center" id="form_spin" role="status" style="display: none;">
            <span class="sr-only">Loading...</span>
          </div>
        <input type="button" class="btn btn-success" value="sent message" id="submit_form">
        
    </form>

    <script>
        $('document').ready(function(){
        $('#submit_form').click(function(){
            if (!($('#name').val()) || !$('#contact').val() ){
                alert('Please fill all details!!!')
                return false;
            }
            // method if empty check robo field is filled
            if ($('#check').val()){
                alert('robo caught')
                return false;
            }
            $('#form_spin').css('display','block')
            $.ajax({
                type:'GET',
                data: {'name': $('#name').val(),
                'contact': $('#contact').val(),
                'email': $('#email').val(),
                'message': $('#message').val(),
                'to_mail': $('#to_mail').val(),
                },
                url:'http://localhost:8000/api/',
                success: function(msg){
                    $('#response_block').html(msg)
                    $('#form_spin').css('display','none')
                    // $('#contact_form')
                }
            })
        })
        })
    </script>

    # ending paste this form to send mail