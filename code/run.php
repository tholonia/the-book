
<?php

$dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
$user = "root";
$passwd = ""; //1q2w3e";
$params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
$dbh = new PDO($dsn, $user, $passwd, $params);

$type = 'pseq';
$lines = gethex(21);

$lineimg = "";
$strong = null;

$bi = array(
    'CONT' => array('L' => "", 'U' => "")
    , 'DEFI' => array('L' => "", 'U' => "")
    , 'NEGO' => array('L' => "", 'U' => "")
);

$res = array(6);

foreach ($lines as $ln) {

    $hexn = $ln['hex'];
    $line = strtoupper($ln['line']);
    $stage = strtoupper($ln['stage']);
    $nature = strtoupper($ln['nature']);
    $state = strtoupper($ln['state']);
    $context = strtoupper($ln['context']);
    $movement = strtoupper($ln['movement']);
    $intention = strtoupper($ln['intention']);
    $concept = strtoupper($ln['concept']);
    $source = strtoupper($ln['source']);
    $expression = strtoupper($ln['expression']);
    $instance = strtoupper($ln['instance']);

    if ($state == "YANG") {
        $lineimg = "------";
    } else {
        $lineimg = "--  --";
    }


    $i1 = "";
    $tri = "";
    if ($state == $nature) {
        $strong = 1;
        $i1 = ", so it is in its natural place, and therefore strong ($strong)";
    } else {
        $strong = 0;
        $i1 = ", so it is NOT in its natural place, and therefore weak ($strong)";
    }




// if (($line == 1) || ($line == 2) || (line == 3)) {
//    $tri = $instance;
//}
// if (($line == 4) || ($line == 5) || ($line == 6)) {
//    $tri = $instance;
//}
    
/*
In hexagram 52, line 4 --  -- is a YIN line occupying a OUTER YIN place of STABILITY , so it is in its natural place, and therefore strong (1). 
This is an OUTER CONTRACTING aspect of the DEFINING side of creation intended to NEGOTIATION and is expressed as COLLECTING.
COLLECTING is also the quality of NEGOTIATION in the trigram of RELEASING.
*/
    
    $str = <<<EOX
        
In hexagram $hexn, line $line $lineimg is a $state line occupying a $context $nature place of $stage $i1. 

The $source side of creation produces an $context $movement through $concept to achieve $intention by $expression 
The is the $intention of $instance.
            
 ($expression is also the quality of $intention in the trigram of $instance.)

EOX;

    $res[$line - 1] = $str;
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
    $str = "$n is very strong because it is a yang line in a yang place and supported by the $n in line 6 which is a yin line in a yin place.\n";
    $res[2] .= $str;
    $str = "$n is very strong because it is a yin line in a yin place and supported by the $n in line 3 which is a yang line in a yang place.\n";
    $res[5] .= $str;
} else {
    if ($bi['CONT']['U'] == 1) {
        $str = "$n is strong in the upper trigram because it is a yin line in yin place.\n";
        $res[5] .= $str;
    }
    if ($bi['CONT']['L'] == 1) {
        $str = "$n is strong in the lower trigram because it is a yang line in a yang place.\n";
        $res[2] .= $str;
    }
}

$str = "";
$n = "DEFINITION";

if ($bi['DEFI']['A'] == 2) {
    $str = "$n is very strong because it is a yin line in a yin place and supported by the $n in line 5 which is a yang line in a yang place.\n";
    $res[1] .= $str;
    $str = "$n is very strong because it is a yang line in a yang place and supported by the $n in line 2 which is a yin line in a yin place.\n";
    $res[4] .= $str;
} else {
    if ($bi['DEFI']['U'] == 1) {
        $str = "$n is strong in the upper trigram because it is is a yang line in a yang place.\n";
        $res[4] .= $str;
    }
    if ($bi['DEFI']['L'] == 1) {
        $str = "$n is strong in the lower trigram because it is is a yin line in a yin place.\n";
        $res[1] .= $str;
    }
}
$str = "";
$n = "NEGOTIATION";
if ($bi['NEGO']['A'] == 2) {
    $str = "$n is very strong because it is a yang line in a yang place and supported by the $n in line 4 which is a yin line in a yin place.\n";
    $res[0] .= $str;
    $str = "$n is very strong because it is a yin line in a yin place and supported by the $n in line 1 which is a yang line in a yang place.\n";
    $res[3] .= $str;
} else {
    if ($bi['NEGO']['U'] == 1) {
        $str = "$n is strong in the upper trigram because it is a yin line in yin place.\n";
        $res[5] .= $str;
    }
    if ($bi['NEGO']['L'] == 1) {
        $str = "$n is strong in the lower trigram because it is a yang line in a yang place.\n";
        $res[2] .= $str;
    }
}


foreach ($res as $r) {
    print "$r\n";
    print "--------------------------------------------------\n";
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
