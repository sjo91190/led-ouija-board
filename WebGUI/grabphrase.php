<?php
 $path = '/home/pi/led-ouija-board/WebGUI/webphrase.txt';
 if (isset($_POST['phrase'])) {
    $fh = fopen($path,"w");
    $string = $_POST['phrase'];
    fwrite($fh,$string);
    fclose($fh);
 }
 header("Location: http://ouijaboard");
 exit();
?>
