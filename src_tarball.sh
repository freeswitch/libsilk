#!/bin/bash
ORIGDIR=`pwd`
TMPDIR=libsilk.$$

mkdir -p ../${TMPDIR}

cd ..
cp -a libsilk ${TMPDIR}/libsilk-1.0.8
cd ${TMPDIR}
rm -rf libsilk-1.0.8/.git*
tar zcvf libsilk-1.0.8.tar.gz libsilk-1.0.8
mv libsilk-1.0.8.tar.gz ${ORIGDIR}/.
cd ${ORIGDIR}
rm -rf ../${TMPDIR}
