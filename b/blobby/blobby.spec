# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%global prerel rc4

Name:           blobby
Version:        1.0
Release:        alt2_0.11.%{prerel}
Summary:        Volley-ball game
Group:          Games/Other
License:        GPLv2+
URL:            http://blobby.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}2-linux-%{version}%{prerel}.tar.gz
Source1:        blobby.desktop
Source2:        blobby.appdata.xml
BuildRequires:  libSDL2-devel libphysfs-devel zlib-devel ctest cmake boost-devel boost-devel-headers boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel zip
BuildRequires:  ImageMagick desktop-file-utils icon-theme-hicolor
Source44: import.info

%description
Blobby Volley is one of the most popular freeware games.
Blobby Volley 2 is the continuation of this lovely game.

%prep
%setup -q -n %{name}-%{version}%{prerel}

# Updated to SDL2 but still looks for SDL also? Why!
sed -ibackup '/find_package(SDL REQUIRED)/d' src/CMakeLists.txt

%build
%{fedora_cmake} .
make %{?_smp_mflags}

%install
%makeinstall_std

# Icon
# unzip -o -j data/gfx.zip gfx/ball01.bmp
convert -size 48x48 -transparent black data/Icon.bmp blobby.png
install -p -m 644 -D blobby.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/blobby.png

# Desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
install -p -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata/blobby.appdata.xml

%files
%doc AUTHORS README ChangeLog COPYING TODO
%{_bindir}/*
%{_datadir}/blobby
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/applications/*.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.11.rc4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.9.rc4
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.8.rc4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.6.rc3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.5.rc3
- update to new release by fcimport

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.4.rc3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.rc1
- update to new release by fcimport

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.1.rc1
- fixed build

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.1.rc1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9c-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.9c-alt1_1
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9b-alt1_2
- converted from Fedora by srpmconvert script

