Summary: ax25 toolls for hamradio.
Name: ax25-tools
Version: 0.0.8
Release: 2
License: LGPL
Group: Applications/Communications
Group(pl): Aplikacje/Komunikacja
Source0: http://prdownloads.sourceforge.net/ax25/ax25-tools-%{version}.tar.gz
BuildRoot: /tmp/%{name}-%{version}-root
ExclusiveArch: %{ix86}
Requires: glibc >= 2.2
Requires: kernel >= 2.2.0
Requires: libtool >= 1.4.2
Requires: libax25 >= 0.0.9
Requires: zlib >= 1.1.3

BuildRequires: libax25-devel
BuildRequires: zlib-devel

%description

Tools for start up ax25 protocole.

%description -l pl

Narzêdzia inicjalizuj±ce protokó³ ax25.

%prep
%setup -q

%build

%configure2_13
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/var/ax25

make DESTDIR=${RPM_BUILD_ROOT} install installconf
gzip -9nf ${RPM_BUILD_ROOT}/usr/share/doc/ax25-tools/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean                                                                          
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/%{_sysconfdir}/ax25/*
/%{_bindir}/*
/%{_sbindir}/*
/%{_docdir}/ax25-tools/*.gz
/%{_mandir}/man[14589]/*.gz
/var/ax25/*
