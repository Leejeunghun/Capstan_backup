<?php

require 'vendor/autoload.php';

use PhpGpio\Gpio;
$gpio = new GPIO();
$gpio->setup(18, 'out');

echo "LED on\n";
$gpio->output(18, 1);

sleep(1);

echo "LED off\n";
$gpio->output(18, 0);

$gpio->unexportAll();
/>
