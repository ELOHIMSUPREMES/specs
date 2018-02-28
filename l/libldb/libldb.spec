%def_enable tests

Name: libldb
Version: 1.1.27
Release: alt1
Summary: A schema-less, ldap like, API and database
License: LGPLv3+
Group: System/Libraries
Url: http://ldb.samba.org/

Source: http://samba.org/ftp/ldb/ldb-%{version}.tar.gz
Source1: ldb-modules.sh

BuildRequires: python-devel python-module-tdb libpytalloc-devel python-module-tevent
BuildRequires: libtalloc-devel libtdb-devel libtevent-devel libpopt-devel libldap-devel xsltproc docbook-style-xsl docbook-dtds

%description
An extensible library that implements and LDAP like API to access remote LDAP
servers, or use local tdb databases.

%package devel
Group: Development/C
Summary: Developer tools for the LDB library
Requires: %name = %version-%release

%description devel
Header files needed to develop programs that link against the LDB library.

%package -n ldb-tools
Group: Development/Tools
Summary: Tools to manage LDB files
Requires: %name = %version-%release

%description -n ldb-tools
Tools to manage LDB files

%package -n python-module-pyldb
Group: Development/Python
Summary: Python bindings for the LDB library
Requires: %name = %version-%release

%description -n python-module-pyldb
Python bindings for the LDB library

%package -n python-module-pyldb-devel
Group: Development/Python
Summary: Development files for the Python bindings for the LDB library
Requires: python-module-pyldb = %version-%release
Requires: %name-devel = %version-%release

%description -n python-module-pyldb-devel
Development files for the Python bindings for the LDB library

%prep
%setup -n ldb-%version

%build
%undefine _configure_gettext
%configure	\
		--disable-rpath \
		--disable-rpath-install \
		--bundled-libraries=NONE \
		--builtin-libraries=replace \
		--with-modulesdir=%_libdir/ldb/modules \
		--with-privatelibdir=%_libdir/ldb
%make

%install
%makeinstall_std

install -D -m755 %SOURCE1 %buildroot%_sysconfdir/bashrc.d/ldb-modules.sh
sed -i s,@libdir@,%_libdir,g %buildroot%_sysconfdir/bashrc.d/ldb-modules.sh

rm -f %buildroot%_libdir/*.a
rm -f %buildroot/%_man3dir/_*

%if_enabled tests
%check
export LD_LIBRARY_PATH=./bin/shared:./bin/shared/private:$LD_LIBRARY_PATH
export LDB_MODULES_PATH=./bin/modules/ldb:$LDB_MODULES_PATH
make test
%endif

%files
%_libdir/libldb.so.*
%dir %_libdir/ldb
%dir %_libdir/ldb/modules
%dir %_libdir/ldb/modules/ldb
%_libdir/ldb/modules/ldb/*.so

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/ldb.pc
%_man3dir/*

%exclude %_includedir/pyldb.h
%exclude %_libdir/libpyldb-util.so

%files -n ldb-tools
%_sysconfdir/bashrc.d/ldb-modules.sh
%_bindir/*
%_man1dir/*
%_libdir/ldb/libldb-cmdline.so

%files -n python-module-pyldb
%python_sitelibdir/ldb.so
%python_sitelibdir/_ldb_text.py*
%_libdir/libpyldb-util.so.1*

%files -n python-module-pyldb-devel
%_includedir/pyldb.h
%_libdir/libpyldb-util.so
%_pkgconfigdir/pyldb-util.pc

%changelog
* Fri Sep 09 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.27-alt1
- Update to new release for samba-4.5.0

* Thu Jun 30 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.26-alt2
- Move ldb-modules.sh from profile.d to bashrc.d to run everywhere

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.26-alt1
- 1.1.26

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.25-alt1
- 1.1.25

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.24-alt1
- 1.1.24
- Security fixes:
  - CVE-2015-5330 (Remote memory read in Samba LDAP server)
  - CVE-2015-3223 (Denial of service in Samba Active Directory server)

* Fri Nov 13 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.23-alt1
- 1.1.23
- Enable tests

* Wed Nov 11 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.21-alt1.1
- Fix path to samba_dsdb.so module (exists only in samba-DC)

* Thu Sep 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.21-alt1
- 1.1.21

* Mon Mar 23 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.20-alt1
- 1.1.20

* Mon Jan 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.19-alt1
- 1.1.19

* Mon Dec 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1.18-alt1
- 1.1.18

* Mon May 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1.17-alt1
- 1.1.17

* Wed Jul 03 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.16-alt1
- 1.1.16

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.15-alt1
- 1.1.15

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Wed Oct 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.13-alt1
- 1.1.13

* Mon Sep 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.12-alt1
- 1.1.12

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Thu Jul 26 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jul 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- rebuild with new libtevent

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Apr 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2
- package python bindings

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt1
- initial build for ALT Linux Sisyphus
