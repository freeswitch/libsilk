Summary:    libsilk is a library for the silk codec
Name:       libsilk
Version:    1.0.8
Release:    1%{?dist}
License:    Skype BSD-like 
Group:      System Environment/Libraries
URL:        http://stash.freeswitch.org
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
Source:     libsilk-1.0.8.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: automake
BuildRequires: libtool

Docdir:     %{_prefix}/doc

%description
libsilk is a library for the silk codec

%package devel
Summary:    silk development files
Group:      Development/Libraries
Requires:   %{name} = %{version}

%description devel
silk development files.

%prep
%setup -q

%build
./bootstrap.sh
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog AUTHORS COPYING NEWS README 

%{_libdir}/libSKP_SILK_SDK.so.*
%{_bindir}/Decoder
%{_bindir}/Encoder
%{_bindir}/signalCompare

%files devel
%defattr(-,root,root,-)
%{_includedir}/silk
%{_libdir}/libSKP_SILK_SDK.a
%{_libdir}/libSKP_SILK_SDK.so
%{_libdir}/pkgconfig/silk.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Thu May 21 2015 Chris Rienzo <chris.rienzo@citrix.com> 1.0.8-1
- Adapted from ilbc.spec for FreeSWITCH dependencies

