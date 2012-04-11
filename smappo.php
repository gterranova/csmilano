<?php
header('Content-type: text/html');

$file = tempnam('/tmp', 'tmp_browser_cookie');
$url = "	http://www.smappo.com/login/";

$postData =  "landpage=%3F&smappo_email=gianpaoloterranova%40gmail.com&smappo_pwd=043373";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_POSTFIELDS, $postData);
curl_setopt($curl, CURLOPT_POST, 1);
curl_setopt($curl, CURLOPT_HEADER, 0);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($curl, CURLOPT_COOKIEJAR, $file);
curl_setopt($curl, CURLOPT_COOKIEFILE, $file);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.3");

curl_close($curl);
unset($curl);

//echo file_get_contents($file);


$ch = curl_init("http://www.smappo.com/attendees/?&e=4e285ee156c95");
 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_COOKIEFILE, $file);
 
$HTTP_Response2 = curl_exec($ch);

$items = explode("<h3>", $HTTP_Response2);

function parse($item) {

  $x = explode("</table></tr></table>", $item);
  preg_match_all("|&nbsp;&nbsp;&nbsp;&nbsp;(.*)</h3>|U",
    $x[0],
    $title, PREG_PATTERN_ORDER);

  $x = preg_replace('/<img[^>]*>/i', '', $x[0]);
  $x = preg_replace('|<a href[^>]*>[^<]*</a>|i', '', $x);
  $x = preg_replace('|&nbsp;|i', '', $x);
  $x = preg_replace('|<td>[0-9\s+/]*|i', '<td>', $x);

  preg_match_all("|<table  width=\"100%\">(.*)</table>|U",
    $x,
    $out, PREG_PATTERN_ORDER);

  echo "<h3>".$title[1][0]."</h3>";
  foreach ($out[0] as $item) {
    echo $item;
  }
}

parse($items[1]);
parse($items[2]);
parse($items[3]);


curl_close($ch);
unset($ch);

unlink($file);
?>