Name: linphone
Version: 3.8.4
Release: alt1
License: GPLv2+
Url: http://www.linphone.org/

Summary: Open source video SIP phone
Group: Communications

Packager: Alexei Takaseev <taf@altlinux.ru>

Source0: %name-%version.tar
#Patch0: %name-%version-%release.patch
BuildPreReq: libortp-devel >= 0.16
BuildRequires: gcc-c++
BuildRequires: doxygen intltool libexosip2-devel libglade-devel libgsm-devel
BuildRequires: libnotify-devel libssl-devel libbelle-sip-devel
BuildRequires: libmediastreamer-devel libreadline-devel libspeex-devel
BuildRequires: libSDL-devel libosip2-devel >= 3.5.0 libncurses-devel
BuildRequires: libxml2-devel

Requires: %name-gui = %version-%release
Requires: %name-cli = %version-%release

%description
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

%package common
Summary: Common files for %name
Group: Communications

%description common
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains common files for %name.

%package gui
Summary: Open source video SIP phone, graphical interface
Group: Communications
Requires: %name-common = %version-%release

%description gui
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains graphical interface of %name.

%package cli
Summary: Open source video SIP phone, console interface
Group: Communications
Requires: %name-common = %version-%release

%description cli
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains console interface for %name.

%package devel
Summary: Development files for %name
Group: Communications

%description devel
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains development files for %name.

%prep
%setup
#%%patch0 -p1
./autogen.sh

%build
%configure --enable-external-ortp \
 --enable-external-mediastreamer \
 --enable-notify \
 --enable-ssl \
 --disable-static
%make_build

%install
%makeinstall_std
%find_lang %name

%files

%files common
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/*.so.*
%exclude %_docdir/%name-%version
%exclude %_datadir/gnome
%exclude %_mandir/cs
%exclude %_man1dir/sipomatic.1.gz

%files gui -f %name.lang
%_bindir/linphone
%_desktopdir/%name.desktop
%_desktopdir/audio-assistant.desktop
%_pixmapsdir/%name
%_man1dir/linphone.1.gz
%_datadir/sounds/%name
%_datadir/%name
%_datadir/appdata/%name.appdata.xml


%files cli
%_bindir/linphonec
%_bindir/linphonecsh
%_bindir/lp-autoanswer
%_bindir/lp-gen-wrappers
%_man1dir/linphonec.1.gz
%_man1dir/linphonecsh.1.gz

%files devel
%doc coreapi/help/doc/html/*
%doc coreapi/help/*.c
%doc coreapi/help/java
%_pkgconfigdir/*
%_includedir/*
%_libdir/*.so
%_datadir/tutorials/%name

%changelog
* Wed Jun 10 2015 Alexei Takaseev <taf@altlinux.org> 3.8.4-alt1
- 3.8.4

* Fri Jun 05 2015 Alexei Takaseev <taf@altlinux.org> 3.8.3-alt1
- 3.8.3

* Fri May 08 2015 Alexei Takaseev <taf@altlinux.org> 3.8.2-alt1
- 3.8.2

* Thu Apr 02 2015 Alexei Takaseev <taf@altlinux.org> 3.8.1-alt1
- 3.8.1

* Fri Mar 13 2015 Alexei Takaseev <taf@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 03 2014 Alexei Takaseev <taf@altlinux.org> 3.7.0-alt2
- update from git:2c0e4947ccfc1ffa98eb88f21ee295cd13f0e5ec

* Wed Feb 26 2014 Alexei Takaseev <taf@altlinux.org> 3.7.0-alt1
- 3.7.0

* Thu Jun 27 2013 Alexei Takaseev <taf@altlinux.org> 3.6.1-alt1
- 3.6.1

* Fri Jun 14 2013 Alexei Takaseev <taf@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Apr 10 2013 Andrey Cherepanov <cas@altlinux.org> 3.5.2-alt2.1
- replace deprecated g_static_mutex* by GMutex

* Thu Oct 11 2012 Alexei Takaseev <taf@altlinux.org> 3.5.2-alt2
- remove deprecated calling g_thread_init

* Sun Jun 24 2012 Alexei Takaseev <taf@altlinux.org> 3.5.2-alt1
- 3.5.2

* Sat Jan 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Fri Jul 22 2011 Egor Glukhov <kaman@altlinux.org> 3.4.3-alt1
- 3.4.3 (Closes: #25054)

* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 3.3.2-alt1.git.88b8d036
- Initial build for Sisyphus
