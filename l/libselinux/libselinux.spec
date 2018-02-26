%def_with python

Name: libselinux
Version: 2.1.12
Release: alt1
Summary: SELinux library
License: Public Domain
Group: System/Libraries
Url: http://userspace.selinuxproject.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%{?_with_python:BuildPreReq: rpm-build-python}
BuildRequires: libpcre-devel libsepol-devel >= 2.1.4
%{?_with_python:BuildRequires: python-dev swig libsepol-devel-static >= 2.1.4}

%description
libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.


%package devel
Summary: SELinux development library and header files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development library and header files needed
for developing SELinux applications.


%package devel-static
Summary: Static SELinux library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static SELinux library needed for developing
statically linked SELinux applications.


%package utils
Summary: SELinux utilities
Group: System/Configuration/Other
Requires: %name = %version-%release

%description utils
This package provides utility programs to get and set process and
file security contexts and to obtain security policy decisions.


%if_with python
%package -n python-module-selinux
%setup_python_module selinux
Summary: Python module for %name
Group: System/Configuration/Other
Requires: %name = %version-%release

%description -n python-module-selinux
This package contains SELinux python bindings.
%endif


%prep
%setup -q
%patch -p1


%build
%make_build CFLAGS="%optflags $(pkg-config libpcre --cflags)" LIBDIR=%_libdir all
%{?_with_python:%make_build CFLAGS="%optflags" LIBDIR=%_libdir pywrap}


%install
%makeinstall_std LIBDIR=%buildroot%_libdir SHLIBDIR=%buildroot/%_lib %{?_with_python:install-pywrap}
install -d -m 0755 %buildroot/var/run/setrans


%post
TELINIT=/sbin/telinit
[ -x $TELINIT -a -L /proc/1/exe -a -L /proc/1/root ] && $TELINIT u ||:


%files
/%_lib/*.so.*
%_man8dir/booleans.*
%_man8dir/selinux.*
%dir /var/run/setrans


%files devel
%_libdir/*.so
%_includedir/selinux
%_pkgconfigdir/*
%_man3dir/*


%files devel-static
%_libdir/*.a


%files utils
%_sbindir/*
%_man5dir/*
%_man8dir/*
%exclude %_man8dir/booleans.*
%exclude %_man8dir/selinux.*


%if_with python
%files -n python-module-selinux
%python_sitelibdir/*
%endif


%changelog
* Sun Sep 23 2012 Led <led@altlinux.ru> 2.1.12-alt1
- 2.1.12
- cleaned up spec

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.98-alt2.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Mikhail Efremov <sem@altlinux.org> 2.0.98-alt2
- Fix License.
- Rebuilt for debuginfo.

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.98-alt1
- Updated to 2.0.98.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt6
- .pc file: use Libs.private instead of Requires.private.

* Mon Sep 13 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt5
- Add /var/run/setrans directory.

* Tue Aug 31 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt4
- Cleanup is_selinux_enabled() (by Dmitry V. Levin).
- Fix %%post to avoid circular dependence on SysVinit (by Dmitry V. Levin).

* Mon Aug 30 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt3
- utils: fix is_selinux_enabled() return value handling.
- Run 'telinit u' in %%post (closes #23987).

* Thu Aug 26 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt2
- Fix errors messages.

* Wed Aug 25 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt1
- Updated to 2.0.96.
- Made 10 symbols hidden (by Dmitry V. Levin).
- Relocated load_setlocaldefs definition (by Dmitry V. Levin).
- Fixed specfile to use %%optflags for build.

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 2.0.94-alt2
- Ugly hackaround for 'load policy' bug.
- fix selinuxenabled.

* Wed Jun 09 2010 Mikhail Efremov <sem@altlinux.org> 2.0.94-alt1
- new version

* Wed Mar 10 2010 Mikhail Efremov <sem@altlinux.org> 2.0.90-alt2
- devel package: fix description and group.
- package the static libraries.

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.90-alt1
- new version

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.80-alt1.1
- Rebuilt with python 2.6

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.80-alt1
- new version

* Tue Jan 13 2009 Anton Farygin <rider@altlinux.ru> 2.0.77-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.76-alt1
- new version

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 2.0.65-alt1
- new (development) version
- specfile cleanup
- use static libsepol for build (mainstream)
- move man3 and man5 to devel package

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.34.15-alt1
- Initial build
