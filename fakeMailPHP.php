<?php
$to      = 'RECIEVER EMAIL ID';
$subject = 'the subject';
$message = 'This is amazing, right!!!';
$headers = 'From: Your_Name<Your_email>' . "\r\n" .
    'Reply-To: YOUR_EMAIL';      //You can also add more headers.


if(mail($to, $subject, $message, $headers)){
echo "Mail Sent";
}
?>
