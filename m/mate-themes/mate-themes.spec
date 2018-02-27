Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%global _internal_version  15baae1

Name:           mate-themes
Version:        1.6.2
Release:        alt1_0.1.git15baae1
Summary:        MATE Desktop themes
License:        GPLv2+
URL:            http://mate-desktop.org

# To generate tarball
# wget http://git.mate-desktop.org/mate-themes/snapshot/%%{name}-{_internal_version}.tar.xz -O %%{name}-%%{version}.git%%{_internal_version}.tar.xz

Source0:       http://raveit65.fedorapeople.org/Mate/git-uptream/%{name}-%{version}.git%{_internal_version}.tar.xz

BuildRequires:  icon-naming-utils
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  mate-icon-theme-devel
BuildRequires:  gtk2-devel
BuildRequires:  libgdk-pixbuf-devel


Requires:       mate-icon-theme
Requires:       libgtk-engines-default
Requires:       libgtk-engine-murrine
# theme engine for BlackMATE and GreenLaguna
Requires: libgtk3-engine-adwaita gnome-themes-standard-data

BuildArch:      noarch
Source44: import.info

%description
MATE Desktop themes


%prep
%setup -q -n %{name}-%{_internal_version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure --enable-all-themes   \
           --enable-test-themes  \
           --enable-icon-mapping \
           --enable-test-themes
make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
%find_lang %{name}


%post
for icon_theme in \
  Fog Quid \
  ContrastHighLargePrint ContrastHighLargePrintInverse \
  ContrastHigh-SVG ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done

%postun
if [ $1 -eq 0 ]; then
for icon_theme in \
  Fog Quid \
  ContrastHighLargePrint ContrastHighLargePrintInverse \
  ContrastHigh-SVG ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done
fi

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/themes/GreenLaguna/
%{_datadir}/themes/Menta/
%{_datadir}/themes/Menta-Black/
%{_datadir}/themes/BlackMATE/
%{_datadir}/themes/Fog/
%{_datadir}/themes/PrintLarge/
%{_datadir}/themes/Quid/
%{_datadir}/themes/Reverse/
%{_datadir}/themes/Shiny/
%{_datadir}/themes/Simply/
%{_datadir}/themes/TraditionalOk/
%{_datadir}/themes/TraditionalGreen/
%{_datadir}/themes/TraditionalOkTest/
%{_datadir}/themes/ContrastHighLargePrint/
%{_datadir}/themes/ContrastHighLargePrintInverse/
%{_datadir}/themes/ContrastLowLargePrint/
%{_datadir}/themes/ContrastLow/
%{_datadir}/themes/ContrastHigh/
%{_datadir}/themes/ContrastHighInverse/
%{_datadir}/icons/ContrastHigh/
%{_datadir}/icons/ContrastHighInverse/
%{_datadir}/icons/ContrastHighLargePrint/
%{_datadir}/icons/ContrastHighLargePrintInverse/
%{_datadir}/icons/ContrastHigh-SVG/
%{_datadir}/icons/Fog/
%{_datadir}/icons/MateLargePrint/
%{_datadir}/icons/Quid/
%{_datadir}/themes/AlaDelta/
%{_datadir}/themes/Atantla/
%{_datadir}/icons/mate/cursors/


%changelog
* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_0.1.git15baae1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Thu Mar 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- converted for ALT Linux by srpmconvert tools

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- converted by srpmconvert script

