<?php
header('Content-type: application/json');

if (strlen($_GET['name']) > 0) {
  $filename = "../public/pages/".$_GET['name'].".txt";
  $f = fopen($filename, "w");
  fwrite($f, stripslashes($_GET['content']));
  fclose($f);
}
echo json_encode($_GET);

?>