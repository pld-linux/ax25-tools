Summary:	ax25 tools for hamradio
Summary(pl.UTF-8):	Narzędzia ax25 dla hamradio
Name:		ax25-tools
Version:	0.0.8
Release:	9
License:	GPL v2+
Group:		Applications/Communications
Source0:	https://downloads.sourceforge.net/ax25/%{name}-%{version}.tar.gz
# Source0-md5:	70172b979b38a9434f21d2e8152f0d5e
Patch0:		%{name}-soundmodem.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-format.patch
Patch3:		%{name}-glibc.patch
Patch4:		%{name}-gcc.patch
URL:		https://ax25.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-devel
BuildRequires:	glibc-devel >= 2.2
BuildRequires:	libax25-devel >= 0.0.9
BuildRequires:	ncurses-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	zlib-devel >= 1.1.3
Requires:	libax25 >= 0.0.9
Requires:	zlib >= 1.1.3
Conflicts:	kernel < 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib

%description
Tools for start up ax25 protocol.

%description -l pl.UTF-8
Narzędzia inicjalizujące protokół ax25.

%package gui
Summary:	FLTK-based GUI tools for AX.25 protocol
Summary(pl.UTF-8):	Oparte na FLTK graficzne narzędzia do protokołu AX.25
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gui
FLTK-based GUI tools for AX.25 protocol.

%description gui -l pl.UTF-8
Oparte na FLTK graficzne narzędzia do protokołu AX.25.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

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
install -d $RPM_BUILD_ROOT{%{_mandir}/man3,%{_localstatedir}/ax25}

%{__make} install installconf \
	DESTDIR=$RPM_BUILD_ROOT

cp -p hdlcutil/baycom.9		$RPM_BUILD_ROOT%{_mandir}/man3/baycom.3
cp -p hdlcutil/hdlcdrv.9	$RPM_BUILD_ROOT%{_mandir}/man3/hdlcdrv.3
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man9

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ax25-tools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog dmascc/README.dmascc tcpip/ttylinkd.{README,INSTALL} user_call/README.user_call yamdrv/README.yamdrv
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/ax25.profile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/ax25d.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/axspawn.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/nrbroadcast
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/rip98d.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/rxecho.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/ttylinkd.conf
%attr(755,root,root) %{_bindir}/mheard
%attr(755,root,root) %{_bindir}/sethdlc
%attr(755,root,root) %{_bindir}/smmixer
%attr(755,root,root) %{_sbindir}/ax25_call
%attr(755,root,root) %{_sbindir}/ax25d
%attr(755,root,root) %{_sbindir}/axctl
%attr(755,root,root) %{_sbindir}/axparms
%attr(755,root,root) %{_sbindir}/axspawn
%attr(755,root,root) %{_sbindir}/beacon
%attr(755,root,root) %{_sbindir}/bpqparms
%attr(755,root,root) %{_sbindir}/dmascc_cfg
%attr(755,root,root) %{_sbindir}/kissattach
%attr(755,root,root) %{_sbindir}/kissnetd
%attr(755,root,root) %{_sbindir}/kissparms
%attr(755,root,root) %{_sbindir}/mcs2h
%attr(755,root,root) %{_sbindir}/mheardd
%attr(755,root,root) %{_sbindir}/mkiss
%attr(755,root,root) %{_sbindir}/net2kiss
%attr(755,root,root) %{_sbindir}/netrom_call
%attr(755,root,root) %{_sbindir}/netromd
%attr(755,root,root) %{_sbindir}/nodesave
%attr(755,root,root) %{_sbindir}/nrattach
%attr(755,root,root) %{_sbindir}/nrparms
%attr(755,root,root) %{_sbindir}/nrsdrv
%attr(755,root,root) %{_sbindir}/rip98d
%attr(755,root,root) %{_sbindir}/rose_call
%attr(755,root,root) %{_sbindir}/rsattach
%attr(755,root,root) %{_sbindir}/rsdwnlnk
%attr(755,root,root) %{_sbindir}/rsmemsiz
%attr(755,root,root) %{_sbindir}/rsparms
%attr(755,root,root) %{_sbindir}/rsuplnk
%attr(755,root,root) %{_sbindir}/rsusers.sh
%attr(755,root,root) %{_sbindir}/rxecho
%attr(755,root,root) %{_sbindir}/spattach
%attr(755,root,root) %{_sbindir}/tcp_call
%attr(755,root,root) %{_sbindir}/ttylinkd
%attr(755,root,root) %{_sbindir}/yamcfg
%{_mandir}/man1/dmascc_cfg.1*
%{_mandir}/man1/mheard.1*
%{_mandir}/man3/baycom.3*
%{_mandir}/man3/hdlcdrv.3*
%{_mandir}/man4/ax25.4*
%{_mandir}/man4/netrom.4*
%{_mandir}/man4/rose.4*
%{_mandir}/man5/ax25d.conf.5*
%{_mandir}/man5/axspawn.conf.5*
%{_mandir}/man5/nrbroadcast.5*
%{_mandir}/man5/rip98d.conf.5*
%{_mandir}/man5/rxecho.conf.5*
%{_mandir}/man5/ttylinkd.conf.5*
%{_mandir}/man8/ax25_call.8*
%{_mandir}/man8/ax25d.8*
%{_mandir}/man8/axctl.8*
%{_mandir}/man8/axparms.8*
%{_mandir}/man8/axspawn.8*
%{_mandir}/man8/beacon.8*
%{_mandir}/man8/bpqparms.8*
%{_mandir}/man8/kissattach.8*
%{_mandir}/man8/kissnetd.8*
%{_mandir}/man8/kissparms.8*
%{_mandir}/man8/mheardd.8*
%{_mandir}/man8/mkiss.8*
%{_mandir}/man8/net2kiss.8*
%{_mandir}/man8/netrom_call.8*
%{_mandir}/man8/netromd.8*
%{_mandir}/man8/nodesave.8*
%{_mandir}/man8/nrattach.8*
%{_mandir}/man8/nrparms.8*
%{_mandir}/man8/nrsdrv.8*
%{_mandir}/man8/rip98d.8*
%{_mandir}/man8/rose_call.8*
%{_mandir}/man8/rsattach.8*
%{_mandir}/man8/rsdwnlnk.8*
%{_mandir}/man8/rsparms.8*
%{_mandir}/man8/rsuplnk.8*
%{_mandir}/man8/rxecho.8*
%{_mandir}/man8/sethdlc.8*
%{_mandir}/man8/smdiag.8*
%{_mandir}/man8/smmixer.8*
%{_mandir}/man8/spattach.8*
%{_mandir}/man8/tcp_call.8*
%{_mandir}/man8/ttylinkd.8*
%dir %{_localstatedir}/ax25/mheard
%config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/ax25/mheard/mheard.dat

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/xfhdlcchpar
%attr(755,root,root) %{_sbindir}/xfhdlcst
%attr(755,root,root) %{_sbindir}/xfsmdiag
%attr(755,root,root) %{_sbindir}/xfsmmixer
