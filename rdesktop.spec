%define	name	rdesktop
%define	version	1.5.0
%define	release	%mkrel 2

Summary:	RDP client
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Terminals
URL:		http://www.rdesktop.org/
Source0:	http://prdownloads.sourceforge.net/rdesktop/%{name}-%{version}.tar.bz2
Patch0: 	rdesktop-fix-depth-crash-1.5.0.patch
BuildRequires:	openssl-devel XFree86-devel gmp-devel libao-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
rdesktop is an open source client for Windows NT Terminal
Server and Windows 2000 Terminal Services, capable of
natively speaking Remote Desktop Protocol (RDP) in order
to present the user's NT desktop. Unlike Citrix ICA, no
server extensions are required.
 
rdesktop currently runs on most UNIX based platforms with
the X Window System, and other ports should be fairly
straightforward.
rdesktop is used through rfbdrake.

%prep
%setup -q

#Fix crash on 16bpp
%patch0  -p1 

# lib64 fix
perl -pi -e "s|\/lib\"|\/%{_lib}\"|g" configure*
perl -pi -e "s|\/lib\ |\/%{_lib}\ |g" configure*

%build

%configure2_5x \
    --with-openssl=%{_prefix} \
    --with-libao=%{_prefix} \
    --with-sound=libao \
    --with-ipv6

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


