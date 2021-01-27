Summary:	RDP client
Name:		rdesktop
Version:	1.9.0
Release:	2
License:	GPL
Group:		Networking/Remote access
URL:		http://www.rdesktop.org/
Source0:	https://github.com/rdesktop/rdesktop/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		rdesktop-libao.patch
Patch1:		rdesktop-1.9.0-rdssl_rkey_get_exp_mod.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(libssl)
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(libgssglue)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  gmp-devel
# nx used to have a forked version of rdesktop called nxdesktop, this
# was dropped in nx 3.2.0 and nx now works with unmodified rdekstop.
# it seems to make most sense handling this by making the original
# rdesktop obsolete and provide the now obsolete fork - AdamW 2008/09
Obsoletes:	nxdesktop < 3.2.0
Provides:	nxdesktop

%description
rdesktop is an open source client for Windows NT Terminal Server and Windows
2000 Terminal Services, capable of natively speaking Remote Desktop Protocol
(RDP) in order to present the user's NT desktop. Unlike Citrix ICA, no server
extensions are required.  

rdesktop currently runs on most UNIX based platforms with the X Window System,
and other ports should be fairly straightforward. rdesktop is used through
rfbdrake.

%prep
%autosetup -p1

# lib64 fix
perl -pi -e "s|\/lib\"|\/%{_lib}\"|g" configure*
perl -pi -e "s|\/lib\ |\/%{_lib}\ |g" configure*

%build
export STRIP="/bin/true"

%configure \
    --with-openssl=%{_prefix} \
    --with-libao=%{_prefix} \
    --with-sound=libao \
    --with-ipv6 \
    --enable-smartcard

%make_build

chmod 644 COPYING
chmod 644 doc/*

%install
%make_install


%files
%doc COPYING doc/*.txt doc/AUTHORS doc/HACKING doc/TODO
%{_bindir}/rdesktop
%{_datadir}/%{name}
%{_mandir}/man1/*
