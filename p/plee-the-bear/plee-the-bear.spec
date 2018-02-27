# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           plee-the-bear
Version:        0.6.0
Release:        alt4_16.1
Summary:        2D platform game
Group:          Games/Other
# Code and artwork respectively
License:        GPLv2+ and CC-BY-SA
URL:            http://plee-the-bear.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/plee-the-bear/Plee%%20the%%20Bear/0.5/%{name}-%{version}-light.tar.gz

# There is probably a more appropriate C++ fix instead of using -fpermissive, but I don't know it.
Patch1:         plee-the-bear-0.6.0-fpermissive.patch
# Disable stupid & broken SVN revision checking
Patch2:         plee-the-bear-0.6.0-svnclawfix.patch
# Initial work taken from Debian, thanks to Konstantinos Margaritis <markos@genesi-usa.com>
Patch3:		plee-the-bear-boost-1.50-patch

BuildRequires:  desktop-file-utils
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires: boost-devel boost-devel-headers boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel
BuildRequires:  wxGTK-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  gettext
BuildRequires: ctest cmake
# There has to be a saner way to remove rpath via cmake...
BuildRequires:	chrpath
Source44: import.info
ExclusiveArch: x86_64

%description
Plee the Bear is a 2D platform game like those we found on consoles in the
beginning of the 90's. The basis of the scenario fit in few lines:

4 PM or so, Plee wakes up, tired. He has dreamed again about that awesome
period when he went across the entire world together with his belle. He
puts his leg in the honey pot... empty! Moreover every single honey pot in
the house is empty. "One more trick of that kid", he thinks. "I'm going to
give him such a wallop of which he sure will remember".

Following honey drops on the ground, Plee reaches the edge of the forest.
Beginning of the game.

The game is led by Julien Jorge and Sebastien Angibaud. Nevertheless, the
game counts several contributions from external people.


%prep
%setup -q
%patch1 -p1 -b .fpermissive
%patch2 -p1 -b .svnclawfix
%patch3 -p1 -b .boost150

%build
%{fedora_cmake}  . \
        -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} \
        -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib}
make %{?_smp_mflags} VERBOSE=1


%install
make install DESTDIR=$RPM_BUILD_ROOT VERBOSE=1 INSTALL="install -p"

# Translations
%find_lang %{name}
%find_lang bear-factory
cat bear-factory.lang >>%{name}.lang
%find_lang bear-engine
cat bear-engine.lang >>%{name}.lang

# Menu entries
for F in $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
do
        desktop-file-validate $F
done

# Nuke the rpaths.
for i in %{buildroot}%{_libdir}/*.so %{buildroot}%{_bindir}/bf-* %{buildroot}%{_bindir}/running-bear; do
	chrpath --delete $i
done


%files -f %{name}.lang
%{_libdir}/*.so
%{_bindir}/*
%{_datadir}/plee-the-bear
%{_datadir}/bear-factory
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
%doc CCPL COPYING GPL 


%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.6.0-alt4_16.1
- rebuild with boost 1.57.0

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_15
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_14
- converted for ALT Linux by srpmconvert tools

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_12
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_11
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_10
- update to new release by fcimport

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_9
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_8
- update to new release by fcimport

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4_7
- rebuild with boost

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt3_7
- rebuild with new boost

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_6
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_5
- update to new release by fcimport

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2_4.1
- Rebuilt with Boost 1.49.0

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_4
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_4
- update to new release by fcimport

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1_1.1
- Rebuilt with Boost 1.48.0

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_1
- update to new release by fcimport

* Fri Jul 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_1
- rebuild with new boost

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_1
- initial release by fcimport

