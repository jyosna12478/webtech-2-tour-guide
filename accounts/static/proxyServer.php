<?php
    header("Content-Type: text/xml");
    $feed = file_get_contents("rss.xml");
    echo $feed;
?>