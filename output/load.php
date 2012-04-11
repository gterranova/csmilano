<?php
header('Content-type: text/html');
header("Cache-Control: no-cache, must-revalidate"); // HTTP/1.1
header("Expires: Sat, 26 Jul 1997 05:00:00 GMT"); // Date in the past

$filename = "../public/pages/".$_GET['name'].".txt";
if (file_exists($filename)) {
  $f = fopen($filename, "r");
  $content = fread($f, filesize($filename));
  fclose($f);
} else {
  $content = "<p></p>";
}
echo $content;

?>