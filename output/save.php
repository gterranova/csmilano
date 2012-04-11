<?php
header('Content-type: text/plain');

if (strlen($_REQUEST['name']) > 0) {
  $filename = "../public/pages/".$_REQUEST['name'].".txt";
  $f = fopen($filename, "w");
  fwrite($f, stripslashes($_REQUEST['content']));
  fclose($f);
}
echo "OK";

?>