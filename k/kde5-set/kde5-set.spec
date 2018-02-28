
Name: kde5-set
Version: 5.5.1
Release: alt1

Group: Graphical desktop/KDE
Summary: Set of KDE 5 applications
License: Public Domain

BuildArch: noarch

%description
%summary

%package -n kde5-runtime
Summary: %summary
Group: Graphical desktop/KDE
Requires: qt5-phonon-backend qt5-quickcontrols qt5-graphicaleffects qt5-imageformats qt5-translations
Requires: kf5-kio kf5-kded kf5-kinit kf5-kwayland-integration
%description -n kde5-runtime
%summary

%package -n kde5-mini
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: qt5-dbus kf5-kde-cli-tools kf5-kwin kf5-plasma-desktop kf5-kinit kf5-kdeclarative
Requires: kde5-dolphin
%description -n kde5-mini
%summary

%package -n kde5-small
Summary: %summary
Group: Graphical desktop/KDE
Requires: icon-theme-breeze
Requires: kde5-mini
Requires: kde5-volume-control
Requires: webclient
Requires: kf5-sddm-kcm kf5-polkit-kde-agent kf5-kio-extras kf5-breeze kf5-oxygen kf5-powerdevil kf5-ksysguard
Requires: kf5-kwallet kf5-kconfig kf5-kglobalaccel kf5-kimageformats
Requires: kde5-ark kde5-konsole kde5-gwenview kde5-okular kde5-kwrite kde5-kwalletmanager
Requires: kde5-kdepasswd kde5-kcalc kde5-kdebugsettings kde5-kross-python
Requires: kf5-milou kf5-systemsettings
%description -n kde5-small
%summary

%package -n kde5
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-normal = %EVR kde5-default = %EVR
Obsoletes: kde5-normal < %EVR kde5-default < %EVR
#Requires: pam0_kwallet5
Requires: kde5-small
Requires: kde5-video-player
Requires: kde5-audio-player
Requires: kde5-network-manager
Requires: kf5-kde-gtk-config kf5-baloo kf5-bluedevil kf5-kscreen kf5-ksshaskpass
Requires: kf5-khotkeys kf5-kinfocenter kf5-kdeplasma-addons
Requires: kde5-khelpcenter kde5-kolourpaint
Requires: kf5-kmenuedit kf5-solid kf5-kdbusaddons kf5-kgamma kf5-plasma-integration
Requires: kde5-kfind kde5-filelight kde5-kcharselect kde5-kteatime kde5-ktimer kde5-spectacle
Requires: kde5-kamera kde5-network-filesharing kde5-ktorrent
%description -n kde5
%summary

%package -n kde5-big
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5
Requires: kde5-email-client
#Requires: kde5-telepathy
Requires: kf5-plasma-workspace-wallpapers
Requires: kf5-kwrited
Requires: kf5-user-manager
Requires: kde5-konversation kde5-kate
Requires: kde5-pim kde5-pim-addons kde5-baseapps kde5-kcron kde5-kruler kde5-ffmpegthumbs
Requires: kf5-plasma-mediacenter kde5-krfb
Requires: kid3-ui-kde5 ring-client-kde5
#Requires: kde5-kipi-plugins-core
%description -n kde5-big
%summary

%package -n kde5-maxi
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-konqueror kde5-dragon kde5-pim-kmail
Requires: kde5-big
Requires: kde5-edu
Requires: kde5-games
Requires: kde5-printing
Requires: kde5-scanning
Requires: kdenlive kde5-connect
Requires: kde5-k3b
#Requires: kde5-digikam kde5-kipi-plugins
%description -n kde5-maxi
%summary

%package -n kde5-somedevel
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: kde5-dolphin-plugins
Requires: kde5-lokalize kde5-okteta kde5-kapptemplate kde5-dev-scripts kde5-kompare
Requires: kde5-sdk-thumbnailers kde5-poxml kde5-umbrello
%description -n kde5-somedevel
%summary

%package -n kde5-edu
Summary: Educational software based on the KDE technologies
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: kde5-kanagram kde5-khangman kde5-parley kde5-kwordquiz kde5-kturtle kde5-marble
Requires: kde5-step kde5-kstars kde5-kig kde5-kmplot kde5-kalgebra kde5-cantor kde5-rocs
Requires: kde5-kbruch kde5-kgeography
#Requires: kde5-minuet
%description -n kde5-edu
Educational software based on the KDE technologies

%package -n kde5-games
Summary: Set of KDE-based games
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: kde5-lskat kde5-kmines kde5-kshisen kde5-ktuberling kde5-bovo kde5-knetwalk
Requires: kde5-katomic kde5-knavalbattle kde5-kpat
%description -n kde5-games
High quality gaming and entertainment software.

%package -n kde5-printing
Summary: Set of printing support applications
Group: Graphics
Requires: kde5-runtime
Requires: kde5-print-manager cups printer-drivers-X11
#system-config-printer-udev
%description -n kde5-printing
KDE printing support applications.

%package -n kde5-scanning
Summary: Set of image scanning support applications
Group: Graphics
Requires: kde5-runtime
Requires: kde5-skanlite hplip-sane libsane-gphoto2 sane
# kde5-ksaneplugin
%description -n kde5-scanning
KDE image scanning support applications.

%files -n kde5-runtime
%files -n kde5-mini
%files -n kde5-small
%files -n kde5
%files -n kde5-big
%files -n kde5-maxi
%files -n kde5-somedevel
%files -n kde5-edu
%files -n kde5-games
%files -n kde5-printing
%files -n kde5-scanning

%changelog
* Tue Sep 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- update requires

* Thu Sep 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- require kde5-email-client for kde5-big

* Tue Aug 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- use digikam, kipi-plugins

* Mon Aug 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- temporary exclude digikam, kipi-plugins

* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- add k3b, digikam, kipi-plugins

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- fix package deskription

* Thu May 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- update requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- update requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt3
- fix requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt2
- fix requires

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- require kde5-audio-player
- update requires

* Tue Apr 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.2-alt1
- update requires

* Fri Apr 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4
- fix requires

* Wed Apr 13 2016 Sergey V Turchin <zerg at altlinux dot org> 5.1.1-alt3
- fix requires

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- fix requires

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- update requires

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt2
- update requires

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- add kde5-edu kde5-games kde5-printing kde5-scanning packages

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt29
- update requires

* Wed Mar 23 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt28
- update requires

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt27
- update requires

* Wed Mar 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt26
- update requires

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt25
- update requires

* Thu Feb 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt24
- update requires

* Mon Feb 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt23
- update requires

* Fri Jan 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt22
- update requires

* Tue Jan 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt21
- update requires

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt20
- update requires

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt19
- fix requires

* Tue Nov 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt18
- update requires

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt17
- update requires

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt16
- update requires

* Fri Oct 02 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt15
- move development tools to separate package

* Thu Oct 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt14
- update requires

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt13
- update requires

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt12
- update requires

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt11
- clean requires

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt10
- update requires

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt9
- update requires

* Thu Aug 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt8
- update requires

* Wed Aug 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt7
- update requires

* Wed Jul 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt6
- update requires

* Wed Apr 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt5
- update requires

* Mon Apr 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt4
- update requires

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt3
- update requires

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt2
- update requires

* Mon Apr 20 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
