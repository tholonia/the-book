#!/usr/bin/php
<?php


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$str = "";
for ($i = 0; $i <=63; $i++) {

    $b = decbin($i);
    $str = $b . $str;
}
print $str."\n";

########

$sAry = str_split($str, 1);

$l = count($sAry);
//print_r($sAry);
print "------------------\n";
$k = 0;
for ($i=$l; $i>=0; $i=$i-3) {
    $c = $i-1;
    $t1 = $sAry[$c-2].$sAry[$c-1].$sAry[$c];
//    $t1 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];

//    $c = $i-2;
//    $t2 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];
//
//    $c = $i-3;
//    $t3 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];
    
//    print "$t1 ;
    print "$k,".bindec($t1)."\n";
    $k++;
//    print "$t1 (".bindec($t1).")\t$t2 (".bindec($t2).")\t$t3 (".bindec($t3).")\t\n";
}


exit;
array_pop($sAry);
$l = count($sAry);
var_export($sAry);

for ($i=$l; $i>0; $i--) {
    $c = $i-1;
    $t1 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];

    $c = $i-2;
    $t2 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];

    $c = $i-3;
    $t3 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];
    
    print "$t1 (".bindec($t1).")\t$t2 (".bindec($t2).")\t$t3 (".bindec($t3).")\t\n";
}


exit;








for ($i=$l; $i>0; $i--) {
    $c = $i-1;
    $t1 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];

    $c = $i-2;
    $t2 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];

    $c = $i-3;
    $t3 = $sAry[$c].$sAry[$c-1].$sAry[$c-2];
    
    print "$t1 (".bindec($t1).")\t$t2 (".bindec($t2).")\t$t3 (".bindec($t3).")\t\n";
}

var_export ($l);