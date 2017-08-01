<?php
$to      = 'YOUR EMAIL ID';
$subject = 'the subject';
$message = 'This is amazing, right!!!';
$headers = 'From: Person_Name<Person_email>' . "\r\n" .
    'Reply-To: YOUR_EMAIL' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();


if(mail($to, $subject, $message, $headers)){
echo "Mail Sent";
}
?>
