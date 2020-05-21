<?php

upd("delete from hex");


for ($i = 0; $i < 64; $i++) {

            for ($j = 1; $j < 7; $j++) {
                upd("insert into hex (hex,line) values ($i,$j) ON DUPLICATE KEY UPDATE hex=$i, line=$j");
            }
    $binary = str_split(strrev(sprintf("%06s", decbin($i))));
//            var_export($binary);

    for ($j = 1; $j < 7; $j++) {
        $c = $j - 1;
                if ($binary[$j - 1] == 1) {
                    upd("update hex set state='yang 1' where hex = $i and line = $j");
                } else {
                    upd("update hex set state='yin 0' where hex = $i and line = $j");
                }
        //------------------------------------
        // set b1
        //------------------------------------
        if (($binary[0] == 0) && ($binary[1] == 0)) {
            $concept = "Absorption 0";
            $source = "Ordering 1";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 1");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 2");

            upd("update hex set expression = 'EARTH 0' where state LIKE 'yin%' and concept LIKE 'Absorption%'");
            upd("update hex set expression = 'Filling 1' where state LIKE 'yang%' and concept LIKE 'Absorption%'");
        }
        if (($binary[0] == 0) && ($binary[1] == 1)) {
            $concept = "Contraction 1";
            $source = "Ordering 1";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 1");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 2");

            upd("update hex set expression = 'WATER 0' where state LIKE 'yin%' and concept LIKE 'Contraction%'");
            upd("update hex set expression = 'Collecting 1' where state LIKE 'yang%' and concept LIKE 'Contraction%'");
        }
        if (($binary[0] == 1) && ($binary[1] == 0)) {
            $concept = "Consumption 0";
            $source = "Chaos 0";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 1");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 2");

            upd("update hex set expression = 'Emptying 0' where state LIKE 'yin%' and concept LIKE 'Consumption%'");
            upd("update hex set expression = 'FIRE 1' where state LIKE 'yang%' and concept LIKE 'Consumption%'");
        }
        if (($binary[0] == 1) && ($binary[1] == 1)) {
            $concept = "Expansion 1";
            $source = "Chaos 0";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 1");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 2");

            upd("update hex set expression = 'Releasing 0' where state LIKE 'yin%' and concept LIKE 'Expansion%'");
            upd("update hex set expression = 'AIR 1' where state LIKE 'yang%' and concept LIKE 'Expansion%'");
        }
        //------------------------------------
        // set b2
        //------------------------------------
        if (($binary[2] == 0) && ($binary[3] == 0)) {
            $concept = "Absorption 0";
            $source = "Ordering 1";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 3");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 4");

            upd("update hex set expression = 'EARTH 0' where state LIKE 'yin%' and concept LIKE 'Absorption%'");
            upd("update hex set expression = 'Filling 1' where state LIKE 'yang%' and concept LIKE 'Absorption%'");
        }
        if (($binary[2] == 0) && ($binary[3] == 1)) {
            $concept = "Contraction 1";
            $source = "Ordering 1";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 3");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 4");

            upd("update hex set expression = 'WATER 0' where state LIKE 'yin%' and concept LIKE 'Contractionv'");
            upd("update hex set expression = 'Collecting 1' where state LIKE 'yang%' and concept LIKE 'Contraction%'");
        }
        if (($binary[2] == 1) && ($binary[3] == 0)) {
            $concept = "Consumption 0";
            $source = "Chaos 0";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 3");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 4");

            upd("update hex set expression = 'Empty 0' where state LIKE 'yin%' and concept LIKE 'Consumption%'");
            upd("update hex set expression = 'FIRE 1' where state LIKE 'yang%' and concept LIKE 'Consumption%'");
        }
        if (($binary[2] == 1) && ($binary[3] == 1)) {
            $concept = "Expansion 1";
            $source = "Chaos 0";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 3");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 4");

            upd("update hex set expression = 'Release 0' where state LIKE 'yin%' and concept LIKE 'Expansionv'");
            upd("update hex set expression = 'AIR 1' where state LIKE 'yang%' and concept LIKE 'Expansion%'");
        }
        //------------------------------------
        // set b3
        //------------------------------------
        if (($binary[4] == 0) && ($binary[5] == 0)) {
            $concept = "Absorption 0";
            $source = "Ordering 1";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 5");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 6");

            upd("update hex set expression = 'EARTH 0' where state LIKE 'yin%' and concept LIKE 'Absorption%'");
            upd("update hex set expression = 'Filling 1' where state LIKE 'yang%' and concept LIKE 'Absorption%'");
        }
        if (($binary[4] == 0) && ($binary[5] == 1)) {
            $concept = "Contraction 1";
            $source = "Ordering 1";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 5");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 6");

            upd("update hex set expression = 'WATER 0' where state LIKE 'yin%' and concept LIKE 'Contraction%'");
            upd("update hex set expression = 'Collecting 1' where state LIKE 'yang%' and concept LIKE 'Contraction%'");
        }
        if (($binary[4] == 1) && ($binary[5] == 0)) {
            $concept = "Consumption 0";
            $source = "Chaos 0";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 5");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 6");

            upd("update hex set expression = 'Empty 0' where state LIKE 'yin%' and concept LIKE 'Consumption%'");
            upd("update hex set expression = 'FIRE 1' where state LIKE 'yang%' and concept LIKE 'Consumption%'");
        }
        if (($binary[4] == 1) && ($binary[5] == 1)) {
            $concept = "Expansion 1";
            $source = "Chaos 0";
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 5");
            upd("update hex set concept = '$concept', source='$source' where hex = $i and line = 6");

            upd("update hex set expression = 'Release 0' where state LIKE 'yin%' and concept LIKE 'Expansion%'");
            upd("update hex set expression = 'AIR 1' where state LIKE 'yang%' and concept LIKE 'Expansion%'");
        }
        if (($binary[0] == 0) && ($binary[1] == 0)&& ($binary[1] == 0)) {        
            upd("update hex set instance = 'EARTH 0' where hex = $i and       (line = 1 OR line =2 OR line = 3)");
        }
        if (($binary[0] == 0) && ($binary[1] == 0)&& ($binary[1] == 1)) {        
            upd("update hex set instance = 'Filling 1' where hex = $i and     (line = 1 OR line =2 OR line = 3)");
        }
        if (($binary[0] == 0) && ($binary[1] == 1)&& ($binary[1] == 0)) {        
            upd("update hex set instance = 'WATER 0' where hex = $i and       (line = 1 OR line =2 OR line = 3)");
        }
        if (($binary[0] == 0) && ($binary[1] == 1)&& ($binary[1] == 1)) {        
            upd("update hex set instance = 'Collecting 1' where hex = $i and  (line = 1 OR line =2 OR line = 3)");
        }
        if (($binary[0] == 1) && ($binary[1] == 0)&& ($binary[1] == 0)) {        
            upd("update hex set instance = 'Emptying 0' where hex = $i and    (line = 1 OR line =2 OR line = 3)");
        }
        if (($binary[0] == 1) && ($binary[1] == 0)&& ($binary[1] == 1)) {        
            upd("update hex set instance = 'FIRE 1' where hex = $i and        (line = 1 OR line =2 OR line = 3)");
        }
        if (($binary[0] == 1) && ($binary[1] == 1)&& ($binary[1] == 0)) {        
            upd("update hex set instance = 'Releasing 0' where hex = $i and     (line = 1 OR line =2 OR line = 3)");
        }
        if (($binary[0] == 1) && ($binary[1] == 1)&& ($binary[1] == 1)) {        
            upd("update hex set instance = 'AIR 1' where hex = $i and         (line = 1 OR line =2 OR line = 3)");
        }
        
        if (($binary[3] == 0) && ($binary[4] == 0)&& ($binary[5] == 0)) {        
            upd("update hex set instance = 'EARTH 0' where hex = $i and (line      = 4 OR line =5 OR line = 6)");
        }
        if (($binary[3] == 0) && ($binary[4] == 0)&& ($binary[5] == 1)) {        
            upd("update hex set instance = 'Filling 1' where hex = $i and (line    = 4 OR line =5 OR line = 6)");
        }
        if (($binary[3] == 0) && ($binary[4] == 1)&& ($binary[5] == 0)) {        
            upd("update hex set instance = 'WATER 0' where hex = $i and (line      = 4 OR line =5 OR line = 6)");
        }
        if (($binary[3] == 0) && ($binary[4] == 1)&& ($binary[5] == 1)) {        
            upd("update hex set instance = 'Collecting 1' where hex = $i and (line = 4 OR line =5 OR line = 6)");
        }
        if (($binary[3] == 1) && ($binary[4] == 0)&& ($binary[5] == 0)) {        
            upd("update hex set instance = 'Emptying 0' where hex = $i and (line   = 4 OR line =5 OR line = 6)");
        }
        if (($binary[3] == 1) && ($binary[4] == 0)&& ($binary[5] == 1)) {        
            upd("update hex set instance = 'FIRE 1' where hex = $i and (line       = 4 OR line =5 OR line = 6)");
        }
        if (($binary[3] == 1) && ($binary[4] == 1)&& ($binary[5] == 0)) {        
            upd("update hex set instance = 'Releasing 0' where hex = $i and (line    = 4 OR line =5 OR line = 6)");
        }
        if (($binary[3] == 1) && ($binary[4] == 1)&& ($binary[5] == 1)) {        
            upd("update hex set instance = 'AIR 1' where hex = $i and (line        = 4 OR line =5 OR line = 6)");
        }
        
    }
}



function upd($sql) {
    $dsn = "mysql:host=localhost;port=3306;dbname=tholonia";
    $user = "root";
    $passwd = ""; //1q2w3e";
    $params = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
    $dbh = new PDO($dsn, $user, $passwd, $params);

    //print "$sql\n";
    $sth = $dbh->prepare($sql);
    $sth->execute();
    $sth->closeCursor();
}
