%define ver_major 3.22
%define domain gcampax.github.com
%define _libexecdir %_prefix/libexec

Name: gnome-shell-extensions
Version: %ver_major.0
Release: alt1

Summary: GNOME Shell Extensions
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/GnomeShell

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gnome-shell >= %ver_major

BuildRequires: gnome-common intltool libgnome-desktop3-devel libgtop-devel

%description
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell.
See %_docdir/%name-%version/README for more information.

%prep
%setup -n %name-%version

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-schemas-compile \
    --enable-extensions=all
%make_build

%check
%make check

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
## Classic mode
%_datadir/gnome-session/sessions/gnome-classic.session
%_datadir/gnome-shell/modes/classic.json
%_datadir/gnome-shell/theme/calendar-today.svg
%_datadir/gnome-shell/theme/classic-toggle-off-intl.svg
%_datadir/gnome-shell/theme/classic-toggle-off-us.svg
%_datadir/gnome-shell/theme/classic-toggle-on-intl.svg
%_datadir/gnome-shell/theme/classic-toggle-on-us.svg
%_datadir/gnome-shell/theme/classic-process-working.svg
%_datadir/gnome-shell/theme/gnome-classic.css
%_datadir/gnome-shell/theme/gnome-classic-high-contrast.css
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.classic-overrides.gschema.xml
%_datadir/xsessions/gnome-classic.desktop

## Extensions
%dir %_datadir/gnome-shell/extensions
# alternate-tab
%dir %_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/prefs.js

# windowsNavigator
%dir %_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/convenience.js

# auto-move-windows
%dir %_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/prefs.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml

# user theme loading
%dir %_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/convenience.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml

# removable drives menu
%dir %_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/convenience.js

# apps-menu
%dir %_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/convenience.js

# native-window-placement
%dir %_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/convenience.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml

# places-menu
%dir %_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/placeDisplay.js

# workspace indicator
%dir %_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/prefs.js

# launch-new-instance
%dir %_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain/stylesheet.css

# window-list
%dir %_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/classic.css
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/prefs.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml

# screenshot-window-sizer
%dir %_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain/stylesheet.css

%doc README

# example
%exclude %_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain/
%exclude %_datadir/glib-2.0/schemas/org.gnome.shell.extensions.example.gschema.xml

%if 0
# xrandr-indicator incompatible with the new DisplayConfig mutter API
%dir %_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/convenience.js
%endif

%changelog
* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Sat Jan 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Fri Oct 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt2
- removed /usr/bin/startgnome-classic

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Jul 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.4-alt1
- 3.14.4

* Sat Dec 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Wed Dec 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt2
- disabled alt-specific mechanism for run gnome-classic session,
  packaged standard xsessions/gnome-classic.desktop instead

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Sep 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3.1-alt1
- 3.8.3.1

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Fri Oct 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0 snapshot

* Wed Mar 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.90-alt1
- 3.3.90 snapshot

* Mon Oct 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- updated from upstream git

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Apr 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- don't package buggy xrandr-indicator

* Thu Apr 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for people/gnome
- don't package gajim integration and example plugins

