Summary:	ax25 tools for hamradio
Summary(pl):	Narzêdzia ax25 dla hamradio
Name:		ax25-tools
Version:	0.0.8
Release:	2
License:	LGPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/ax25/%{name}-%{version}.tar.gz
BuildRequires:	libax25-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}
Requires:	glibc >= 2.2
Requires:	kernel >= 2.2.0
Requires:	libtool >= 1.4.2
Requires:	libax25 >= 0.0.9
Requires:	zlib >= 1.1.3

%description
Tools for start up ax25 protocol.

%description -l pl
Narzêdzia inicjalizuj±ce protokó³ ax25.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/ax25

%{__make} DESTDIR=$RPM_BUILD_ROOT install installconf
gzip -9nf $RPM_BUILD_ROOT%{_datadir}/doc/ax25-tools/*

%clean                                                                          
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_sysconfdir}/ax25/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%docdir %{_docdir}/ax25-tools
%dir %{_docdir}/ax25-tools
%{_docdir}/ax25-tools/*.gz
%{_mandir}/man[14589]/*
/var/ax25/*
