
$document.ready(function(){
    $('#example-form').submit(function(event){
        $.ajax({
            url:$(this).attr('action'),
            type:$(this).attr('method'),
            data:$(this).serialize(),}
            success:function(response){
                console.log(response);
                
            }
        })
    })
   
})
/** $(document).ready(function() {
    $('#example-form').on('submit', function(e) {
        e.preventDefault(); // Prevent default form submission
console.log("in ajax content of this:", this, this.action)
      // $(this).attr('action')
        $.ajax({
            url:$(this).attr('action'),
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                console.log(response);
                // Handle successful form submission
              if (response.redirected && response.url)
              {
              
              $('main').html(response);
              console.log("success:" );}
              
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error("error: ",error);
            }
        });
    });
});*/

/*document.getElementById('example-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    var formData = new FormData(this); // Collect form data

    fetch('/register', {
        method: 'POST',
        body: formData,
    })
   .then(response => response.json())
   .then(data => {
        if (data.account_created) {
            alert('Account created successfully!');
            // Optionally, redirect to the home page or update the UI as needed
        } else if (data.error) {
            alert('Registration failed: ' + data.error);
        }
    })
   .catch(error => console.error('Error:', error));
});*/

/*document.getElementById('example-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    try {
        var formData = new FormData(this); // Collect form data

        fetch('/register', {
            method: 'POST',
            body: formData,
        })
       .then(response => response.json()) // Parse JSON response
       .then(data => {
            if (data.account_created) {
                alert('Account created successfully!');
                // Optionally, redirect to the home page or update the UI as needed
            } else if (data.error) {
                alert('Registration failed: ' + data.error);
            }
        })
       .catch(error => console.error('Error:', error)); // Catch any errors during fetch
    } catch (error) {
        console.error('Error:', error); // Catch any errors in the try block
    }
});

  

