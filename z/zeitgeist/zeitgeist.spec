%define major 0.9
%define api_ver 2.0
%define _noarchpkgconfigdir %_datadir/pkgconfig

Name: zeitgeist
Version: %major.12
Release: alt1

Summary: Framework providing Desktop activity awareness

Group: Office
License: LGPLv3+ and LGPLv3
# zeitgeist/loggers/iso_strptime.py is LGPLv3 and the rest LGPLv3+
Url: https://launchpad.net/zeitgeist

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://launchpad.net/%name/%major/%version/+download/%name-%version.tar
Patch: %name-0.9.12-alt-python3_syntax.patch

Requires: lib%name%api_ver = %version-%release

%define vala_ver 0.18
%define tp_glib_ver 0.18

# can't do buildreq correctly
BuildRequires: python-devel python-module-rdflib
BuildRequires: raptor
BuildRequires: gettext perl-XML-Parser intltool gtk-doc
BuildRequires: gcc-c++ glib2-devel libsqlite3-devel libgio-devel libdbus-devel libxapian-devel
BuildRequires: libgtk+3-devel libjson-glib-devel
BuildRequires: libtelepathy-glib-devel >= %tp_glib_ver
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools >= %vala_ver libtelepathy-glib-vala
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-rdflib
# for autoreconf
BuildRequires: gettext-tools

%description
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

Note that this package only contains the daemon, which you can use
together with several different user interfaces.

%package -n lib%name%api_ver
Summary: Dynamic library to access the Zeitgeist daemon
Group: System/Libraries

%description -n lib%name%api_ver
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package contains the dynamic Zeitgeist library, which provides
access to the Zeitgeist daemon.

%package -n lib%name%api_ver-devel
Summary: Development files for Zeitgeist
Group: Development/C
Requires: lib%name%api_ver = %version-%release

%description -n lib%name%api_ver-devel
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package contains the development files for the Zeitgeist library.

%package -n lib%name%api_ver-gir
Summary: GObject introspection data for the Zeitgeist library
Group: System/Libraries
Requires: lib%name%api_ver = %version-%release

%description -n lib%name%api_ver-gir
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides GObject introspection data for the Zeitgeist library.

%package -n lib%name%api_ver-gir-devel
Summary: GObject introspection devel data for the Zeitgeist library
Group: Development/Other
BuildArch: noarch
Requires: lib%name%api_ver-gir = %version-%release
Requires: lib%name%api_ver-devel = %version-%release

%description -n lib%name%api_ver-gir-devel
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides GObject introspection devel data for the Zeitgeist library.

%package -n python-module-%name%api_ver
Summary: Python bindings for the Zeitgeist library
Group: Development/Python
BuildArch: noarch
Requires: lib%name%api_ver = %version-%release

%description -n python-module-%name%api_ver
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides Python2 bindings for the Zeitgeist library.

%package -n python3-module-%name%api_ver
Summary: Python3 bindings for the Zeitgeist library
Group: Development/Python3
BuildArch: noarch
Requires: lib%name%api_ver = %version-%release

%description -n python3-module-%name%api_ver
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides Python3 bindings for the Zeitgeist library.

%package -n lib%name%api_ver-devel-doc
Summary: Development documentation for lib%name%api_ver
Group: Development/Documentation
Conflicts: lib%name%api_ver < %version
BuildArch: noarch

%description -n lib%name%api_ver-devel-doc
This package contains development documentation for the Zeitgeist library.


%prep
%setup
%setup -D -c
mv %name-%version py3build
pushd py3build
%patch
popd

%build
%autoreconf
%configure --disable-static PYTHON=%__python
%make_build

pushd py3build
%autoreconf
%configure --disable-static \
    --enable-gtk-doc \
    PYTHON=/usr/bin/python3
%make_build
popd

%install
%makeinstall_std
pushd py3build
%makeinstall_std
popd

rm -rf %buildroot%_prefix/doc/

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/%name-daemon
%_bindir/%name-datahub
%_datadir/%name/
%_datadir/dbus-1/services/org.gnome.%name.service
%_man1dir/%name-*.*
%_sysconfdir/xdg/autostart/zeitgeist-datahub.desktop
%_datadir/bash-completion/completions/%name-daemon

%files -n python-module-%name%api_ver
%python_sitelibdir_noarch/zeitgeist/

%files -n python3-module-%name%api_ver
%python3_sitelibdir_noarch/zeitgeist/

%files -n lib%name%api_ver
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name%api_ver-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi
%_vapidir/%name-datamodel-%api_ver.vapi

%files -n lib%name%api_ver-gir
%_typelibdir/Zeitgeist-2.0.typelib

%files -n lib%name%api_ver-gir-devel
%_girdir/Zeitgeist-2.0.gir

%if 0
%files -n lib%name%api_ver-devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.12-alt1
- 0.9.12
- fixed syntax for python3

* Wed Mar 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.10-alt1
- 0.9.10
- removed upstreamed -link.patch
- updated buildreqs
- new libzeitgeist2.0{,-devel}, libzeitgeist2.0-gir{,-devel} subpackages
- prepared libzeitgeist2.0-devel-doc subpackage
- python bindings moved to separate noarch subpackages

* Sun Jun 10 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9.0.1-alt1
- new version 0.9.0.1 (with rpmrb script)

* Tue Jan 24 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.2-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Deji Akingunola <dakingun@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3.1-1
- Update to 0.3.3.1 to fix datasource_registry bug (BZ #586238)

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Wed Jan 20 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Thu Jan 14 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1-1
- Add missing requires (Package reviews)
- Update license tag (Package reviews)
- Update to latest release

* Tue Dec 01 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Nov 04 2009 Deji Akingunola <dakingun@gmail.com> - 0.2.1-1
- Initial Fedora packaging

