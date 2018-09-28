#/bin/sh

apt-get -y install build-essential devscripts
mk-build-deps --install --remove debian/control --tool "apt-get -y --no-install-recommends"
apt-get -y -f install
debuild -us -uc -b -I.git -i'\.git/'
