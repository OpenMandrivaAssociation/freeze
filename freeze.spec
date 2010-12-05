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
