<?php
//header('Content-type: application/json');

$filename = "../public/pages/".$_GET['name'].".txt";
if (file_exists($filename)) {
  $f = fopen($filename, "r");
  $content = fread($f, filesize($filename));
  fclose($f);
} else {
  $content = "";
}
echo $content;

?>