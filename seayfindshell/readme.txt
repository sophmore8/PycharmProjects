程序开源地址：

1.这款查杀程序采用插件化实现，可以对新型的web后门添加自定义的查杀插件，现有的10余款插件已经能够查杀目前常见的大部分web后门，不过要注意的是现有的插件大多数都是查杀PHP后门的，asp及aspx不在覆盖范围，jsp的插件较少，因为当初写这个程序是为了解决linux下的webshell查杀问题。

2.智能查杀，这款查杀程序实现了读PHP的变量简单跟踪，能够查杀大量变异后门，比如

<?php
$a=$_POST['a'];
#fdsffd
$b='feafdea';
assert($a);
?>

这类的后门，程序会自动追踪assert函数内的$a变量输入来源，如果发现参数可控，则会报警。当然它还支持include、file_put_contents等后门查杀。



3.加密后门查杀，这款查杀程序收集了大量加密后门特征，能够将加密后门精确识别并查杀，像zend加密、base64等加密都有专门的查杀插件。




4.针对PHP动态函数后门，由于PHP函数名可以当成字符串来改变的特性，导致查杀关键字很难定位，这款程序有专门针对PHP动态函数后门的插件。



5.针对型查杀插件，这款程序有专门针对PHPDDOS后门的查杀功能，集合了目前常见的PHPDDOS脚本特征
11

6.根据文件最后修改时间查找后门，为了照顾到小白服务器管理员，特意加入了根据文件最后修改时间查找后门文件，默认程序只会查找php和jsp文件的最后修改时间，如有需要查找其他扩展名的文件，只需要修改main.py即可。
88


7. 人性化显示，根据本人这几年的应急响应经验，本程序会自动输出我们需要的信息，包括后门路径、后门描述、后门代码以及文件最后修改时间。

本人目前收集的webshel数百个webshell已经覆盖绝大部分。