
Summary: Extracts attachments out of mailpack format emails
Name: ripole
Version: 0.2.2
Release: alt1
License: BSD
Group: Networking/Mail
Url: http://www.pldaniels.com/ripole/
Packager: Alexey Shabalin <shaba@altlinux.org>
Source0: http://www.pldaniels.com/ripole/%name-%version.tar.gz
Patch0: ripole-%version-shared.patch

%description
ripOLE is a small program/library designed to pull out attachments from OLE2
data files (ie, MS Office documents).

%package -n lib%name
Summary: Shared %name library
Group: System/Libraries

%description -n lib%name
ripOLE is a small program/library designed to pull out attachments from OLE2
data files (ie, MS Office documents). ripOLE is BSD licenced meaning that
commercial projects can also use the code without worry of licence costs or
legal liabilities.

%package -n lib%name-devel
Summary: Development files for the %name library
Group: Development/C
Provides: %name-devel
PreReq: lib%name = %version-%release

%description -n lib%name-devel
ripOLE is a small program/library designed to pull out attachments from OLE2
data files (ie, MS Office documents). ripOLE is BSD licenced meaning that
commercial projects can also use the code without worry of licence costs or
legal liabilities.

This package contains the development files for ripOLE.

%prep
%setup
%patch0 -p2

%build
%undefine __libtoolize
%make \
CFLAGS="$CFLAGS -I. -fPIC -DPIC -D_REENTRANT" \
    libdir=%_libdir

%install
%makeinstall

%files
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*
%_libdir/*.so
%exclude %_libdir/*.a

%changelog
* Thu Apr 25 2013 Ildar Mulyukov <ildar@altlinux.ru> 0.2.2-alt1
- new version

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.0-alt3.qa1
- NMU: rebuilt for set-versioned provides.

* Thu Jul 02 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt3
- rewrite patch0 and specify a tag with `--tag'

* Fri Jul 20 2007 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt2
- fix build on x86_64 (change %%make_install to %%makeinstall)

* Fri Jul 20 2007 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial build for Altlinux

