Summary:	RDP client
Name:		rdesktop
Version:	1.9.0
Release:	1
License:	GPL
Group:		Networking/Remote access
URL:		http://www.rdesktop.org/
Source0:	https://github.com/rdesktop/rdesktop/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		rdesktop-libao.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(ao)
BuildRequires:	openssl-devel
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

%setup -q
%patch0 -p1 -b .ao

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


%changelog
* Wed Jan 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.1-1
+ Revision: 759737
- version update 1.7.1

* Mon May 30 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-2
+ Revision: 681867
- sync with fedora

* Mon Apr 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-1
+ Revision: 655850
- 1.7.0

* Thu Feb 10 2011 Funda Wang <fwang@mandriva.org> 1.6.0-13
+ Revision: 637086
- rebuild
- tighten BR

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 1.6.0-12mdv2011.0
+ Revision: 574310
- rebuild for new pcsclite

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 1.6.0-11mdv2010.1
+ Revision: 533136
- Rebuild for new openssl

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 1.6.0-10mdv2010.1
+ Revision: 528352
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-9mdv2010.1
+ Revision: 511634
- rebuilt against openssl-0.9.8m

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.6.0-8mdv2010.0
+ Revision: 426879
- rebuild

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-7mdv2009.1
+ Revision: 337182
- keep bash completion in its own package

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-6mdv2009.1
+ Revision: 317574
- rebuild

* Tue Oct 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-5mdv2009.1
+ Revision: 293569
- bash completion

* Fri Sep 05 2008 Adam Williamson <awilliamson@mandriva.org> 1.6.0-4mdv2009.0
+ Revision: 280996
- obsolete and provide nxdesktop (a fork of rdesktop for nx which was dropped
  as of nx 3.2.0)

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.6.0-3mdv2009.0
+ Revision: 265621
- rebuild early 2009.0 package (before pixel changes)

* Thu May 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-2mdv2009.0
+ Revision: 207645
- revert back to using libao for sound support

* Thu May 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1mdv2009.0
+ Revision: 207585
- 1.6.0
- use alsa instead of libao for sound support
- enable smartcard support
- drop the redundant rdesktop-fix-depth-crash-1.5.0.patch patch

* Wed Jan 09 2008 Michael Scherer <misc@mandriva.org> 1.5.0-4mdv2008.1
+ Revision: 147225
- fix Group, patch from Shlomi Fish, fix bug #36375

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Fri Sep 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-3mdv2008.0
+ Revision: 85742
- try to restore the original changelog that was lost somehow...

* Wed Jun 13 2007 Emmanuel Blindauer <blindauer@mandriva.org> 1.5.0-2mdv2008.0
+ Revision: 38544
- add patch to fix problem #30452, rdesktop crashing on 16 bits display with win2k3 server

