# For build on x86_64 fix (via macros?)
#gpointer knop=gtk_object_get_user_data(GTK_OBJECT(widget));
#switch ((gint)knop)

%define build_lang uk_UA.KOI8-U

%define oname iceBw
%define oversion 9_11

Name:    icebw
Version: 9.11
Release: alt1
Summary: Free financial accounting system with GTK interface

Group:   Office
License: GPL
Url:     http://www.iceb.net.ua

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %url/download/%name-%oversion.tar.bz2

BuildRequires: gcc-c++ libMySQL-devel libgtk+3-devel

%description
Free financial accounting system.

%prep
%setup -q -c
subst "s|/usr/share/locale/ru/|%buildroot%_datadir/locale/uk/|g" locale/Makefile

%build
export LANG=%build_lang
%make_build

%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/locale/uk/LC_MESSAGES/
make install install \
    BINDIR=%buildroot%_bindir

%files
%_bindir/*
%_datadir/locale/uk/LC_MESSAGES/%oname.mo

%changelog
* Thu Feb 27 2014 Andrey Cherepanov <cas@altlinux.org> 9.11-alt1
- New version
- Fix project URL

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 7.0-alt1.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Wed Aug 31 2011 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1
- New version 7.0

* Tue Apr 19 2011 Andrey Cherepanov <cas@altlinux.org> 6.11-alt1
- New version 6.11

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 6.1-alt1
- 6_1

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- initial build for ALT Linux Sisyphus

