<?php
 $path = 'webphrase.txt';
 if (isset($_POST['phrase'])) {
    $fh = fopen($path,"w");
    $string = $_POST['phrase'];
    fwrite($fh,$string);
    fclose($fh);
 }
 header("Location: localhost:8000/landing.html");
 exit();
?>
