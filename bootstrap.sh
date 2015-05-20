#!/bin/bash
libtoolize=`which glibtoolize` || `which libtoolize`
aclocal
$libtoolize -i --copy
autoconf
autoheader
automake --add-missing
