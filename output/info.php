<?php
//header('Content-type: text/plain');

$url = "http://www.couchsurfing.org/meetings.html?mid=109902&show_members=Yes";
$str = file_get_contents($url);

$str = substr($str, strpos($str, "csmap.init({")+11);
$str = substr($str, 0, strpos($str, "});")+1);

$obj = json_decode($str);

$list = array();

foreach ($obj as $lt) {
  $cn += 0;
  foreach ($lt as $ln) {
      $list[$ln->c][$ln->l] = $ln->u;
    }
}

ksort($list);


foreach ($list as $country=>$value) {
  echo "<div class='column span-13 last'><div class='column span-4'><h2>$country</h2></div><div class='column span-9 last'><div class='column span-5'>";
  $cur = 0;
  foreach ($value as $city=>$users) {
    foreach ($users as $user) {
      echo "<a href='http://www.couchsurfing.org/profile.html?id=".$user->u."' target='_blank'>".ucwords(strtolower($user->n))."</a>\n";
      $cur++;
      if ($cur %2) { echo "</div><div class='column span-4 last'>";}
      else { echo "</div><div class='column span-5'>"; }
    }
  }
  echo "</div></div>";
  echo "<p>&nbsp;</p><hr />";
}

?>