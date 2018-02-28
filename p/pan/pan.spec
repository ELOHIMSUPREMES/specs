# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate gcc-c++ pkgconfig(gtk+-3.0) pkgconfig(gtkspell3-3.0) pkgconfig(webkitgtk-3.0) pkgconfig(zlib)
# END SourceDeps(oneline)
Summary:	A Usenet newsreader for GNOME/GTK+
Name:		pan
Version:	0.140
Release:	alt2_1
Epoch:		1
License:	GPLv2
Group:		Networking/WWW
Source0:	http://pan.rebelbase.com/download/releases/%{version}/source/%{name}-%{version}.tar.bz2
URL:		http://pan.rebelbase.com/
BuildRequires:	desktop-file-utils
BuildRequires: gettext-tools libasprintf-devel
BuildRequires:	intltool >= 0.40.6
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libgmime-devel libgmime-gir-devel
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires:	libgtkspell-devel >= 2.0.7
BuildRequires:	libenchant-devel >= 1.6.0
BuildRequires:	libappstream-glib
BuildRequires: libnotify-devel libnotify-gir-devel
BuildRequires: libgnome-keyring-devel libgnome-keyring-gir-devel
# In the past, we could not link GPLv2-only Pan with GnuTLS due to libgnutls being effectively LGPLv3+
# However, the GnuTLS libs are now clearly LGPLv2+, which is compatible.
BuildRequires: libgnutls-devel libgnutlsxx-devel
Source44: import.info

%description
Pan is a Usenet newsreader which attempts to be pleasant to
new and advanced users alike. It has all the standard
newsreaders features and also supports offline reading,
scoring and killfiles, yEnc, NZB, PGP handling, multiple
servers, and secure connections. It is also the only Unix
newsreader to get a perfect score on the Good Net-Keeping
Seal of Approval evaluations.

%prep
%setup -q

sed -i -e 's|StartupNotify=false|StartupNotify=true|' %{name}.desktop.in

%build
%configure --without-gtk3 --with-gnutls \
    --with-dbus --with-gmime-crypto \
    --with-gtkspell --enable-libnotify \
    --enable-gkr

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.140-alt2_1
- to Sisyphus for TDE

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.140-alt1_1
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.140-alt1_0.2.20160114git
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.139-alt1_10
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.139-alt1_8
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.139-alt1_7
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.139-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.139-alt1_5
- update to new release by fcimport

* Wed May 22 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.139-alt1_4
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.139-alt1_3
- initial fc import

