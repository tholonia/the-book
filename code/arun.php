#!/usr/bin/php
<?php
$R = chr(27) . "[91m"; //Red foreground
$G = chr(27) . "[32m"; //Green foreground
$Y = chr(27) . "[33m"; //Yellow foreground
$B = chr(27) . "[36m"; //Blue foreground
$O = chr(27) . "[0m";


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




$stage = "";
$nature = "";
$context = "";
$movement = "";
$intention = "";
$li = 1;

    $upper = getTri("U",$hexnum);
    $lower = getTri("L",$hexnum);
    

foreach ($lines as $ln) {
    $thislineAry = getlineattr($li);
    
        $tri = $lower;
    if ($li > 3) {
        $tri = $upper;
    }

//    var_export($ln);
//    var_export($thislineAry);

    $stage = strtoupper($thislineAry[0]['stage']);
    $nature = strtoupper($thislineAry[0]['nature']);
    $context = strtoupper($thislineAry[0]['context']);
    $movement = strtoupper($thislineAry[0]['movement']);
    $intention = strtoupper($thislineAry[0]['intention']);
    $phrase = strtoupper($thislineAry[0]['phrase']);
    $keyword = strtoupper($thislineAry[0]['keyword']);
    $name = strtoupper($thislineAry[0]['name']);



    print $G;
    print "Line $li:\n$stage of $tri is a $context $nature place with the intention to $intention by '$phrase $keyword' ($name)\n";
    print $O;



//    // now get the hex
//    
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


    //print "\t Occupied by [[$state \n";

    if ($state != $nature) {
        $alt = getsql("SELECT * FROM signs WHERE sign = '" . ($li + 6) . "'");

        $ALT_stage = strtoupper($alt[0]['stage']);
        $ALT_nature = strtoupper($alt[0]['nature']);
        $ALT_context = strtoupper($alt[0]['context']);
        $ALT_intention = strtoupper($alt[0]['intention']);
        $ALT_phrase = strtoupper($alt[0]['phrase']);
        $ALT_keyword = strtoupper($alt[0]['keyword']);
        $ALT_name = strtoupper($alt[0]['name']);


        print $R;
        print "$ALT_stage is a $ALT_context $ALT_nature place with the intention to $ALT_intention by '$ALT_phrase $ALT_keyword' ($ALT_name)\n";
        PRINT $O;
        print $B;
        print "$stage of $tri $intention by $Y $phrase by $ALT_phrase $R and $Y $ALT_keyword within $keyword $R\n";
        PRINT $O;
    } else {


        print $B;
        print "$stage of $tri $intention $tri by $phrase  $keyword\n";
        PRINT $O;
    }

    print "\n";

    $li++;
}

function term($k, $fld) {
    $M = chr(27) . "[95m"; //Red background
    $G = chr(27) . "[32m"; //Green background
    $O = chr(27) . "[0m";
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
    return($M . $f . "$G");
}

function getlineattr($line) {
    $dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
    $user = "root";
    $passwd = ""; //1q2w3e";
    $params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
    $dbh = new PDO($dsn, $user, $passwd, $params);
    $sql = <<<EOX
            
SELECT * 
FROM
signs
INNER JOIN hex_attr_th ON hex_attr_th.context = signs.context AND hex_attr_th.stage = signs.stage
WHERE
hex_attr_th.line = $line
         
EOX;
    //print $sql . "\n";
    $sth = $dbh->prepare($sql);
    $sth->execute();
    $ids = $sth->fetchAll();
    $c = array();
    return($ids);
}

function getsql($sql) {
    $dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
    $user = "root";
    $passwd = ""; //1q2w3e";
    $params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
    $dbh = new PDO($dsn, $user, $passwd, $params);
    //print $sql . "\n";
    $sth = $dbh->prepare($sql);
    $sth->execute();
    $ids = $sth->fetchAll();
    $c = array();
    return($ids);
}

function gethex($hexn) {
    $dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
    $user = "root";
    $passwd = ""; //1q2w3e";
    $params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
    $dbh = new PDO($dsn, $user, $passwd, $params);
    $sql = <<<EOX
SELECT
hex_th.hex,
hex_th.state,
hex_th.concept,
hex_th.source,
hex_th.expression,
hex_th.instance,
hex_attr_th.line,
hex_attr_th.stage,
hex_attr_th.nature,
hex_attr_th.context,
hex_attr_th.context2,
hex_attr_th.movement,
hex_attr_th.intention
FROM
hex_th
INNER JOIN hex_attr_th ON hex_th.line = hex_attr_th.line
WHERE
hex_th.hex = $hexn
ORDER BY
hex_attr_th.line ASC           
EOX;
    $sth = $dbh->prepare($sql);
    $sth->execute();
    $ids = $sth->fetchAll();
    $c = array();
    return($ids);
}


function getTri($ul, $hex) {
    $bn = str_split(sprintf("%06s",decbin($hex)),1);
    rsort($bn);
    $a = str_split(implode("",$bn),3);
    var_export($a);
 
    $s = 0;
    if ($ul == "U") {
        $s = 1;
    }
    $rs = $a[$s];
$tri = null;
    switch($rs) {
        case "000":
            $tri = "Absorbing EARTH (foundation, source of growth)";
            break;
        case "001":
            $tri = "Absorbing Filling (with resources and life)";
            break;
        case "010":
            $tri = "Contracting WATER (downward moving,negative energy)";
            break;
        case "011":
            $tri = "Contracting Collecting (always returns)";
            break;
        case "100":
            $tri = "Consuming Emptying (transforming, from one state to another)";
            break;
        case "101":
            $tri = "Consuming FIRE (upward moving, positive enery)";
            break;
        case "110":
            $tri = "Expanding Releaseing (filling all space)";
            break;
        case "111":
            $tri = "Expanding AIR (direction and potential for growth)";
            break;
        
        
    } 
    return($tri);
}