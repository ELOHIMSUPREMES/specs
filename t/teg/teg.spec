# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize ElectricFence gcc-c++ libreadline-devel perl(Text/Wrap.pm) python-devel
# END SourceDeps(oneline)
%define fedora 19
Name:           teg
Version:        0.11.2
Release:        alt2_31
Summary:        Turn based strategy game
Group:          Games/Other
License:        GPLv2
URL:            http://teg.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        teg.desktop
Patch0:         teg_libxml.patch
#Patch1:         teg_themes.patch
#Patch2:         teg-disable-help.patch
Patch3:		teg_fixwording.patch
Source2:         teg-fix-help.patch

BuildRequires:  tidy glib2-devel libxml2-devel libgnomeui-devel
BuildRequires:  gettext
BuildRequires:  perl(XML/Parser.pm)
BuildRequires:  desktop-file-utils
Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2
Source44: import.info

%description
Tenes Empanadas Graciela is a clone of Plan TA.ctico y EstratA.gico de la 
Guerra, a turn based strategy game. Some rules are different.

%prep
%setup -q 
%patch0 -p1
#%patch2 -p1
%patch3 -p1
for file in AUTHORS COPYING README TODO PEOPLE ChangeLog; do
    iconv -f iso8859-1 -t utf-8 < $file > $file.$$
    mv -f $file.$$  $file
done

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/gconf/gconf.xml.defaults
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mv -f $RPM_BUILD_ROOT/%{_datadir}/pixmaps/teg_icono.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/teg.png
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gnome/apps/Games/teg.desktop
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
                 \
%endif
  --dir=$RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE1}
patch -p1 < %{SOURCE2}
mv -f $RPM_BUILD_DIR/%{?buildsubdir}/docs/gnome-help/C/teg.sgml $RPM_BUILD_ROOT/%{_datadir}/gnome/help/teg/C/teg.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README TODO PEOPLE ChangeLog
%{_bindir}/tegrobot
%{_bindir}/tegclient
%{_bindir}/tegserver
%{_datadir}/pixmaps/teg_pix/
%{_datadir}/pixmaps/teg.png
%{_datadir}/gnome/help/teg/
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/teg.desktop
%else
%{_datadir}/applications/teg.desktop
%endif
%{_sysconfdir}/gconf/schemas/teg.schemas

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/teg.schemas >/dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/teg.schemas > /dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/teg.schemas > /dev/null || :

%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_31
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_30
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_29
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_28
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_27
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_27
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_26
- updated by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_25
- initial release by fcimport

