Name: 	 redshift
Version: 1.8
Release: alt1

Summary: Redshift adjusts the color temperature of your screen
Summary(ru_RU.UTF-8): Redshift изменяет температуру цвета вашего экрана для снижения утомляемости глаз

License: GPLv3+
Group: 	 Graphical desktop/GNOME
Url: 	 http://jonls.dk/redshift/

Packager: Anton Chernyshov <ach@altlinux.org>
Source0:  %name-%version.tar

Patch1:   %name-geoclue-provider.patch

BuildPreReq: libGConf-devel
BuildPreReq: libXrandr-devel
BuildPreReq: libXxf86vm-devel
BuildPreReq: libgeoclue-devel
BuildPreReq: gettext-devel
#BuildPreReq: xorg-xf86vidmodeproto-devel

%description
Redshift adjusts the color temperature of your screen according
to your surroundings. This may help your eyes hurt less if you
are working in front of the screen at night. The color temperature
is set according to the position of the sun. A different color
temperature is set during night and daytime. During twilight and early
morning, the color temperature transitions smoothly from night
to daytime temperature to allow your eyes to slowly adapt.

%description -l ru_RU.UTF-8
Redshift изменяет температуру цвета экрана вашего компьютера. Это может
снизить утомляемость глаз, особенно если вы работаете за компьютером
ночью. Температура цвета устанавливается в зависимости от позиции
солнца на небе (определяется на основе географических координат)
и текущего времени суток. Изменение температуры цвета происходит
плавно, давая Вашим глазам время на адаптацию.

%prep
%setup
%patch1 -p1
%autoreconf

%build
%configure \
    --enable-randr \
    --enable-vidmode \
    --enable-nls \
    --enable-gui \
    --enable-gnome-clock \
    
%make_build

%install
%makeinstall_std
test %_libdir = /usr/lib64 && mv %buildroot/%_libexecdir %buildroot/%_libdir
%find_lang %name

%files -f %name.lang
%_bindir/*
%python_sitelibdir/%{name}_gtk/*
%_desktopdir/*
%doc ABOUT-NLS AUTHORS NEWS README
%_iconsdir/hicolor/*
%_man1dir/*

%post
# If gnome-panel installed (i.e for GNOME users) - set program to autostart
# KDE users must set redshift parameters manually
if [ -e %_desktopdir/gnome-panel.desktop ]; then
	cp %_desktopdir/gtk-redshift.desktop %_sysconfdir/xdg/autostart/
fi

%postun
rm -f %_sysconfdir/xdg/autostart/gtk-redshift.desktop

%changelog
* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 1.8-alt1
- New version

* Wed Jul 31 2013 Andrey Cherepanov <cas@altlinux.org> 1.7-alt1
- New version

* Thu Apr 11 2013 Andrey Cherepanov <cas@altlinux.org> 1.6-alt3.2
- Remove requires of deprecated gnome-panel

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt3.1
- Rebuild with Python-2.7

* Sat Nov 12 2010 Anton Chernyshov <ach@altlinux.org> 1.6-alt3
- remove unneeded stuff from spec
- remove linking with .la-files (and create patch for this)

* Mon Oct 18 2010 Anton Chernyshov <ach@altlinux.org> 1.6-alt2
- minor spec modifications
- exclude license from package according to distribution policy
- include man page

* Mon Oct 18 2010 Anton Chernyshov <ach@altlinux.org> 1.6-alt1
- new upstream release
- completely translate this release to Russian language
- added new BuildReq dependencies

* Sat Oct 16 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt3.1
- completely translate program to Russian language

* Thu Oct 14 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt3
- adding some configure settings
- reformed and corrected Russian translation files

* Mon Oct 11 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt2.1
- some minor spec changes

* Tue Oct 7 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt2
- fix up spec-file according to Sisyphus requirements

* Wed Oct 6 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt1
- create (more or less) generic spec file and initial build...
