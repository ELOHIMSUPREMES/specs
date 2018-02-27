
Name: accerciser
Version: 3.12.0
Release: alt1

Summary: An interactive Python tool for querying accessibility information
Url: http://live.gnome.org/Accerciser
License: %bsd

Group: Accessibility
Packager: Michael Pozhidaev <msp@altlinux.ru>

# use python3
AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Sun Sep 28 2008
BuildRequires: GConf docbook-dtds gnome-doc-utils-xslt perl-XML-Parser python3-devel libgio-devel libgtk+3-devel python3-module-pyatspi

BuildRequires: rpm-build-licenses rpm-build-gnome gnome-doc-utils libGConf-devel
BuildPreReq: intltool itstool python3-module-pygobject3-devel
BuildRequires: desktop-file-utils libat-spi2-core-devel

BuildArch: noarch
Source: %name-%version.tar

Requires: python3-module-%name = %version-%release

%description
An interactive Python accessibility explorer.

#%add_python3_req_skip gtksourceview

%package -n python3-module-%name
Summary: Python module for accerciser
Group: Development/Python
BuildArch: noarch
# The macro below is resolved into an empty string but confuses build process
#%_python_set_noarch

%description -n python3-module-%name
An interactive Python accessibility explorer.

This package contains Python module for accerciser.

%prep
%setup

%build
%configure --without-pyreqs
%make_build

%install
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=X-Development-Accessibility \
        %buildroot%_desktopdir/%name.desktop

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS README COPYING NEWS ChangeLog
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_man1dir/*
%_datadir/glib-2.0/schemas/*
%_datadir/icons/hicolor/16x16/apps/%name.png
%_datadir/icons/hicolor/22x22/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/48x48/apps/accerciser.png
%_datadir/icons/hicolor/scalable/apps/accerciser.svg
%_datadir/icons/HighContrast/scalable/apps/accerciser.svg

%files -n python3-module-%name
%python3_sitelibdir/%name/

%changelog
* Mon Apr 14 2014 Paul Wolneykien <manowar@altlinux.org> 3.12.0-alt1
- Fresh up to v3.12.0 with the help of cronbuild and update-source-functions.

* Wed Mar 12 2014 Paul Wolneykien <manowar@altlinux.org> 3.8.2-alt2
- Update the sources via script. Skip unstable branches.

* Tue May 14 2013 Paul Wolneykien <manowar@altlinux.org> 3.8.2-alt1
- new version 3.8.2

* Wed Apr 10 2013 Paul Wolneykien <manowar@altlinux.ru> 3.8.0-alt1
- Build with Python 3.
- New version 3.8.0.

* Sat Nov 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Clean spec

* Fri Nov 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Version 3.6.2 (ALT #28019)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12.1-alt5.1
- Rebuild with Python-2.7

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt5
- updated watch file, updated future BuildRequires: for 3.2.x version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt4
- added future BuildRequires: for 3.2.x version

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt3
- find_lang finds gnome_helpdir, no need to package it explicitly

* Mon Oct 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2
- use find_lang, updated desktop file categories

* Sun Oct 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1
- intermediate update to 1.12.1. added watch file.

* Sun Oct 10 2010 Michael Pozhidaev <msp@altlinux.ru> 1.11.1-alt1
- New version 1.11.1 (closes: #23423)

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt1
- Version 1.9.3

* Thu Mar 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3
- Extracted python module into separate package

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.1
- Rebuilt with python 2.6

* Wed Oct 15 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt2
- Fixed gconf schema installation

* Sun Sep 28 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt1
- ALT Linux package

* Thu Apr 12 2007 Peter Parente <parente@cs.unc.edu>
- Added gconf schema install, uninstall, and files

* Mon Apr 02 2007 Peter Parente <parente@cs.unc.edu>
- Added without-pyreqs flag to avoid checking for modules at rpmbuild time
- Added locales to files section

* Wed Feb 22 2007 Peter Parente <parente@cs.unc.edu>
- First release
