Summary:	RDP client
Name:		rdesktop
Version:	1.6.0
Release:	%mkrel 2
License:	GPL
Group:		Networking/Remote access
URL:		http://www.rdesktop.org/
Source0:	http://prdownloads.sourceforge.net/rdesktop/%{name}-%{version}.tar.gz
BuildRequires:	alsa-lib-devel
BuildRequires:	gmp-devel
BuildRequires:	libao-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	openssl-devel
BuildRequires:	pcsc-lite-devel >= 1.2.9
BuildRequires:	pkgconfig
BuildRequires:	X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
rdesktop is an open source client for Windows NT Terminal Server and Windows
2000 Terminal Services, capable of natively speaking Remote Desktop Protocol
(RDP) in order to present the user's NT desktop. Unlike Citrix ICA, no server
extensions are required.  

rdesktop currently runs on most UNIX based platforms with the X Window System,
and other ports should be fairly straightforward. rdesktop is used through
rfbdrake.

%prep

%setup -q

# lib64 fix
perl -pi -e "s|\/lib\"|\/%{_lib}\"|g" configure*
perl -pi -e "s|\/lib\ |\/%{_lib}\ |g" configure*

%build
export STRIP="/bin/true"

%configure2_5x \
    --with-openssl=%{_prefix} \
    --with-libao=%{_prefix} \
    --with-sound=libao \
    --with-ipv6 \
    --enable-smartcard

%make

chmod 644 COPYING
chmod 644 doc/*

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING doc/*.txt doc/AUTHORS doc/HACKING doc/TODO
%{_bindir}/rdesktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/keymaps
%{_mandir}/man1/*
