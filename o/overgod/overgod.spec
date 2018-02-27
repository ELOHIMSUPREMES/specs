Name:           overgod
Version:        1.0
Release:        alt2_17
Summary:        Another arcade-style shoot-em-up
Group:          Games/Other
License:        GPLv2+
URL:            http://www.allegro.cc/depot/Overgod
Source0:        http://downloads.sourceforge.net/overgod/overgod.tar.gz
Source1:        overgod.desktop
Source2:        overgod.png
Patch0:         overgod-1.0.patch
BuildRequires:  liballegro-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
For too long has humanity been ruled by cruel and disputatious gods!
Fly through the various layers of the Celestial Oversphere to unseat
those who control the universe.

In Overgod you control a little vehicle in the middle of the screen and fly
around and shoot things - a bit like asteroids, but the asteroids move
independently and shoot back. You can also upgrade your vehicle in various
ways.


%prep
%setup -q
%patch0 -p1 -z .unix
sed -i 's/\r//' readme.txt licence.txt

# as-needed
sed -i -e 's,$(CC) $(LDFLAGS) -o $@ $^,$(CC) -o $@ $^ $(LDFLAGS),' Makefile


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" PREFIX=%{_prefix}


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps


%files
%doc readme.txt licence.txt
%{_bindir}/overgod
%{_datadir}/overgod
%{_datadir}/applications/*overgod.desktop
%{_datadir}/icons/hicolor/48x48/apps/overgod.png


%changelog
* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_17
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_15
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_14
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_13
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_12
- initial release by fcimport

