# BEGIN SourceDeps(oneline):
BuildRequires: libSDL-devel
# END SourceDeps(oneline)
%define fedora 19
Name:           dd2
Version:        0.2.2
Release:        alt2_10
Summary:        Dodgin' Diamond 2 - Shoot'em up arcade game
Group:          Games/Other
License:        GPLv2+
URL:            http://www.usebox.net/jjm/dd2/
Source0:        http://www.usebox.net/jjm/dd2/releases/dd2-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         dd2-0.2.1-glob-highscore.patch
Patch1:         dd2-0.2.1-640x480-fullscreen.patch
BuildRequires:  libSDL_mixer-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
This is a little shoot'em up arcade game for one or two players. It aims to
be an 'old school' arcade game with low resolution graphics, top-down scroll
action, energy based gameplay and different weapons with several levels of
power.


%prep
%setup -q
%patch0 -p1 -z .highscore
%patch1 -p1 -z .fs
#stop autoxxx from rerunning
touch src/data/Makefile.in


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/games
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-hiscore \
  $RPM_BUILD_ROOT%{_var}/games

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
              \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/%{name}.png


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/games/%{name}-hiscore


%changelog
* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_7
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_6
- converted from Fedora by srpmconvert script

