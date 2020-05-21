#!/usr/bin/php
<?php

$R = chr(27)."[91m"; //Red background
$G = chr(27)."[32m"; //Green background
$Y = chr(27)."[33m"; //Yellow background
$B = chr(27)."[36m"; //Blue background
$O = chr(27)."[0m";


$hexnum = $argv[1];
$dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
$user = "root";
$passwd = ""; //1q2w3e";
$params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
$dbh = new PDO($dsn, $user, $passwd, $params);

$type = 'pseq';
$lines = gethex($hexnum);

$lineimg = "";
$strong = null;

$bi = array(
    'CONT' => array('L' => "", 'U' => "")
    , 'DEFI' => array('L' => "", 'U' => "")
    , 'NEGO' => array('L' => "", 'U' => "")
);

$res = array(6);
$strongAry = array(6);
$fmtstrAry = array();

$li = 1;
foreach ($lines as $ln) {

    $hexn = $ln['hex'];
    $line = strtoupper($ln['line']);
    $stage = strtoupper($ln['stage']);
    $state = strtoupper($ln['state']);

    $NATURE = strtoupper($ln['nature']);
    $CONTEXT = strtoupper($ln['context']);
    $MOVEMENT = strtoupper($ln['movement']);
    $INTENTION = strtoupper($ln['intention']);

    $concept = strtoupper($ln['concept']);
    $source = strtoupper($ln['source']);
    $expression = strtoupper($ln['expression']);
    $instance = strtoupper($ln['instance']);

    $fmt = "";
    if ($state == "YANG 1") {
//        $lineimg = "======";
        $lineimg = "<img src='../Images/bc/yang.png' style='width:30px'>";
        $fmt = "####";
    } else {
//        $lineimg = "==  ==";
        $lineimg = "<img src='../Images/bc/yin.png' style='width:30px'>";
    }

    $fmtstrAry[$li] = "$fmt **$line** $lineimg ";
    
    $i1 = "";
    $tri = "";
    if ($state == $NATURE) {
        $strong = 1;
        $i1 = ", so it is in its natural place, and therefore it is a strong [$state]";
    } else {
        $strong = 0;
        $i1 = ", so it is NOT in its natural place, and therefore it is a weak [$state]";
    }
    $strongAry[$li] = $strong;
    $li++;

//- From [$INTENTION $source] emerges [$CONTEXT $concept] of [$stage] which creates [$NATURE $expression] that appear as [$MOVEMENT $instance] 
    $nl="";
    $tb="";
    $te="";

//    $nl="\n";
//    $tb="\t\t${O}";
//    $te=$G;

    $str = "\n";
    $str .= "$R**Line $line** $lineimg is a [$state] line occupying a [$CONTEXT $NATURE] place of [$stage] $i1. \n$O";
    $str .= "$R**Line $line** $lineimg is a [$state] line occupying a [". term("$CONTEXT $NATURE","dsc") ."] place of [". term("$stage","dsc") ."] $i1. \n$O";
    $str .= "$G- From [$INTENTION $source] emerges ${nl}[$CONTEXT $concept] of [$stage] which creates [$NATURE $expression] that appear as [$MOVEMENT $instance] \n$O";
    $str .= "$G- #### From [". term("$INTENTION $source","dsc") ."] emerges [ ". term("$CONTEXT $concept","dsc") ."] of [$stage] which creates [ ". term("$NATURE $expression","dsc") ."] that appear as [ ". term("$MOVEMENT $instance ","dsc") ."]\n$O";


    $res[$line - 1] = $str;
}

$lstr = "";
$strongStr = array(6);
//1

for ($i = 1; $i < 4; $i++) {
    $lline = $i ;
    $uline = $lline + 3;
    if (($strongAry[$i] == 1) && ($strongAry[$i + 3] == 1)) {
        $lstr = $B."- A strong line $lline is further supported by a strong line $uline.$O";
        $strongStr[$i] = $lstr;
    }
    if (($strongAry[$i] == 0) && ($strongAry[$i + 3] == 1)) {
        $lstr = $B."- Line $lline is weak, but it is supported by a strong line $uline.$O";
        $strongStr[$i] = $lstr;
    }
    if (($strongAry[$i] == 1) && ($strongAry[$i + 3] == 0)) {
        $lstr = $B."- Line $lline is strong, but it is hindered by a weak line $uline.$O";
        $strongStr[$i] = $lstr;
    }
}
for ($i = 4; $i < 7; $i++) {
    $lline = $i ;
    $uline = $lline - 3;
    if (($strongAry[$i] == 1) && ($strongAry[$i - 3] == 1)) {
        $lstr = $B."- A strong line $lline is further supported by a strong line $uline.$O";
        $strongStr[$i] = $lstr;
    }
    if (($strongAry[$i] == 0) && ($strongAry[$i - 3] == 1)) {
        $lstr = $B."- Line $lline is weak, but it is supported by a strong line $uline.$O";
        $strongStr[$i] = $lstr;
    }
    if (($strongAry[$i] == 1) && ($strongAry[$i - 3] == 0)) {
        $lstr = $B."- Line $lline is strong, but it is hindered by a weak line $uline.$O";
        $strongStr[$i] = $lstr;
    }
}




/////////////////////////////////////////////////////////


$Dstr = null;
$Cstr = null;
$Nstr = null;
$Dhi = null;
$Chi = null;
$Nhi = null;
$Dlo = null;
$Clo = null;
$Nlo = null;

$bi = array(
    'CONT' => array('L' => "0", 'U' => "0", 'A' => "0")
    , 'DEFI' => array('L' => "0", 'U' => "0", 'A' => "0")
    , 'NEGO' => array('L' => "0", 'U' => "0", 'A' => "0")
);

if ($lines[0]['nature'] == $lines[0]['state']) {
    $bi['NEGO']['L'] = 1;
}
if ($lines[1]['nature'] == $lines[1]['state']) {
    $bi['DEFI']['L'] = 1;
}
if ($lines[2]['nature'] == $lines[2]['state']) {
    $bi['CONT']['L'] = 1;
}
if ($lines[3]['nature'] == $lines[3]['state']) {
    $bi['NEGO']['U'] = 1;
}
if ($lines[4]['nature'] == $lines[4]['state']) {
    $bi['DEFI']['U'] = 1;
}
if ($lines[5]['nature'] == $lines[5]['state']) {
    $bi['DEFI']['U'] = 1;
}

$bi['CONT']['A'] = $bi['CONT']['L'] + $bi['CONT']['U'];
$bi['DEFI']['A'] = $bi['DEFI']['L'] + $bi['DEFI']['U'];
$bi['NEGO']['A'] = $bi['NEGO']['L'] + $bi['NEGO']['U'];


$str = "";
$n = "CONTRIBUTION";

if ($bi['CONT']['A'] == 2) {
    $str = $Y . "- $n is very strong because it is a yang line in a yang place and supported by the $n in line 6 which is a yin line in a yin place.$O";
    $res[2] .= $str;
    $str = $Y . "- $n is very strong because it is a yin line in a yin place and supported by the $n in line 3 which is a yang line in a yang place.$O";
    $res[5] .= $str;
} else {
    if ($bi['CONT']['U'] == 1) {
        $str = $Y . "- $n is strong in the upper trigram because it is a yin line in yin place.$O";
        $res[5] .= $str;
    }
    if ($bi['CONT']['L'] == 1) {
        $str = $Y . "- $n is strong in the lower trigram because it is a yang line in a yang place.$O";
        $res[2] .= $str;
    }
}

$str = "";
$n = "DEFINITION";

if ($bi['DEFI']['A'] == 2) {
    $str = $Y . "- $n is very strong because it is a yin line in a yin place and supported by the $n in line 5 which is a yang line in a yang place.$O";
    $res[1] .= $str;
    $str = $Y . "- $n is very strong because it is a yang line in a yang place and supported by the $n in line 2 which is a yin line in a yin place.$O";
    $res[4] .= $str;
} else {
    if ($bi['DEFI']['U'] == 1) {
        $str = $Y . "- $n is strong in the upper trigram because it is is a yang line in a yang place.$O";
        $res[4] .= $str;
    }
    if ($bi['DEFI']['L'] == 1) {
        $str = $Y . "$n is strong in the lower trigram because it is is a yin line in a yin place.$O";
        $res[1] .= $str;
    }
}
$str = "";
$n = "NEGOTIATION";
if ($bi['NEGO']['A'] == 2) {
    $str = $Y . "- $n is very strong because it is a yang line in a yang place and supported by the $n in line 4 which is a yin line in a yin place.$O";
    $res[0] .= $str;
    $str = $Y . "- $n is very strong because it is a yin line in a yin place and supported by the $n in line 1 which is a yang line in a yang place.$O";
    $res[3] .= $str;
} else {
    if ($bi['NEGO']['U'] == 1) {
        $str = $Y . "- $n is strong in the upper trigram because it is a yin line in yin place.$O";
        $res[5] .= $str;
    }
    if ($bi['NEGO']['L'] == 1) {
        $str = $Y . "- $n is strong in the lower trigram because it is a yang line in a yang place.$O";
        $res[2] .= $str;
    }
}


asort($res);
$i=1;
foreach ($res as $r) {
    print "$r";
    print "\n";
    print $strongStr[$i];
    print "\n";
    $i++;

}

$fmtstrAry = array_reverse($fmtstrAry,false);
foreach ($fmtstrAry as $r) {
    print "\n$r\n";
}

function term($k,$fld) {
$M = chr(27)."[95m"; //Red background
$G = chr(27)."[32m"; //Green background
$O = chr(27)."[0m";    
    $dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
    $user = "root";
    $passwd = ""; //1q2w3e";
    $params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
    $dbh = new PDO($dsn, $user, $passwd, $params);
    $sql = "SELECT terms.dsc FROM terms WHERE terms.`key` = '$k'"; 
    $sth = $dbh->prepare($sql);
    $sth->execute();
    $ids = $sth->fetchAll();
    $c = array();
    $f = $ids[0][$fld];
    if ($f == "") {
        $f = "??????????????";
    }
    return($M.$f."$G");
}

function gethex($hexn) {
    $dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
    $user = "root";
    $passwd = ""; //1q2w3e";
    $params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
    $dbh = new PDO($dsn, $user, $passwd, $params);
    $sql = <<<EOX
SELECT
hex.hex,
hex.state,
hex.concept,
hex.source,
hex.expression,
hex.instance,
hex_attr.line,
hex_attr.stage,
hex_attr.nature,
hex_attr.context,
hex_attr.context2,
hex_attr.movement,
hex_attr.intention
FROM
hex
INNER JOIN hex_attr ON hex.line = hex_attr.line
WHERE
hex.hex = $hexn
ORDER BY
hex_attr.line DESC           
EOX;
    $sth = $dbh->prepare($sql);
    $sth->execute();
    $ids = $sth->fetchAll();
    $c = array();
    return($ids);
}
