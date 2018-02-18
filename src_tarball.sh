#!/bin/bash
ORIGDIR=`pwd`
TMPDIR=libsilk.$$

mkdir -p ../${TMPDIR}

cd ..
cp -a libsilk ${TMPDIR}/libsilk-1.0.9
cd ${TMPDIR}
rm -rf libsilk-1.0.9/.git*
tar zcvf libsilk-1.0.9.tar.gz libsilk-1.0.9
mv libsilk-1.0.9.tar.gz ${ORIGDIR}/.
cd ${ORIGDIR}
rm -rf ../${TMPDIR}
