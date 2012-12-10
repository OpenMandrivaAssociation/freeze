Summary:	Freeze/melt/fcat compression utilities
Name:		freeze
Version:	2.5.0
Release:	%mkrel 7
Group:		Archiving/Compression
License:	Distributable
# No one agrees on the canonical download site, everyone uses the same version
Source:		http://www.ibiblio.org/pub/Linux/utils/compress/freeze-2.5.0.tar.gz
Patch0:		freeze-2.5.patch
Patch1:		freeze-2.5.0-printf.patch
Patch2:		freeze-2.5.0-deffile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Freeze is an old file compressor and decompressor that is not in common use
anymore, but can be useful if the need ever arises to dearchive files
compressed with it.

%prep

%setup -q
%patch0 -p1 -b .Makefile
%patch1 -p1 -b .printf
%patch2 -p1 -b .deffile

%build
chmod u+x configure
%configure
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

%makeinstall \
    MANDEST="%{buildroot}%{_mandir}/man1/"

### Fix symlinks properly
for bin in fcat melt unfreeze; do
    ln -sf freeze %{buildroot}%{_bindir}/$bin
    rm -f %{buildroot}%{_mandir}/man1/$bin.1
    ln -sf freeze.1.bz2 %{buildroot}%{_mandir}/man1/$bin.1.bz2
done

%clean
rm -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc MANIFEST README
%attr(0755,root,root) %{_bindir}/*
%doc %{_mandir}/man?/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.0-7mdv2011.0
+ Revision: 610771
- rebuild

* Mon Dec 07 2009 Jérôme Brenier <incubusss@mandriva.org> 2.5.0-6mdv2010.1
+ Revision: 474570
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.5.0-4mdv2009.0
+ Revision: 245411
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.5.0-2mdv2008.1
+ Revision: 170846
- rebuild
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 2.5.0-1mdv2008.0
+ Revision: 34918
- Import freeze



* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 2.5.0-1mdv2008.0
- initial Mandriva package (fedora extras import)

* Sat Sep 02 2006  Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 2.5.0-7
- FE6 Rebuild

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 2.5.0-6
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 26 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 2.5.0-5
- rebuild with gcc 4.1

* Sat Jul 23 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- 2.5.0-4
- Fix bad printf string (#149613).
- Fix default cnf file location in readme and man page.
- Don't strip.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 11 2004 Michael Schwendt <mschwendt[AT]users.sf.net>
- 2.5.0-0.fdr.2
- Build with rpm opt flags.

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 
- 0:2.5.0-0.fdr.1
- Fedorization

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com>
- 2.5-2
- Cosmetic rebuild for Group-tag.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com>
- 2.5-1
- Initial package. (using DAR)
