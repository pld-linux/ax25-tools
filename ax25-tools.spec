# TODO: FHS (/var/ax25 -> /var/lib/ax25(?))
Summary:	ax25 tools for hamradio
Summary(pl):	Narzêdzia ax25 dla hamradio
Name:		ax25-tools
Version:	0.0.8
Release:	3
License:	LGPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ax25/%{name}-%{version}.tar.gz
URL:		http://ax25.sourceforge.net/
BuildRequires:	libax25-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
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

%{__make} install installconf \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc dmascc/README.dmascc tcpip/ttylinkd.{README,INSTALL}
%doc user_call/README.user_call
%{_sysconfdir}/ax25/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%docdir %{_docdir}/ax25-tools
%dir %{_docdir}/ax25-tools
%{_mandir}/man[14589]/*
# NOT FHS-compliant
/var/ax25/*
