Summary:	ax25 tools for hamradio
Summary(pl):	Narzêdzia ax25 dla hamradio
Name:		ax25-tools
Version:	0.0.8
Release:	5
License:	LGPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ax25/%{name}-%{version}.tar.gz
# Source0-md5:	70172b979b38a9434f21d2e8152f0d5e
Patch0:		%{name}-linux26.patch
URL:		http://ax25.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libax25-devel
BuildRequires:	zlib-devel
Requires:	glibc >= 2.2
Requires:	libax25 >= 0.0.9
Requires:	zlib >= 1.1.3
Conflicts:	kernel < 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreq	libfltk.so.1
%define		_localstatedir	/var/lib

%description
Tools for start up ax25 protocol.

%description -l pl
Narzêdzia inicjalizuj±ce protokó³ ax25.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/ax25

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
%{_localstatedir}/ax25/*
