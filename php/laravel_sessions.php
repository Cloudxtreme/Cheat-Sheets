<?php
// add
Session::put('key', 'value');
session(['key' => 'value']);

// get
$value = Session::get('key');
$value = session('key');

// get and forget
$value = Session::pull('key', 'default');

// remove
Session::forget('key');

// remove all
Session::flush();

// session just for next request
Session::flash('key', 'value');
Session::reflash(); // one more time
Session::keep(['username', 'email']); // reflash just username
