Name: giggle
Version: 0.7
Release: alt2

Summary: Giggle is a Gtk frontend to git.
License: GPL
Group: Development/Other

URL: http://live.gnome.org/giggle
Source: %name-%version.tar
# from fedora
Patch: %name-0.7-fc-gtksourceview.patch

Requires: git-core

BuildRequires: git-core libgtksourceview3-devel intltool gnome-common libvte3-devel yelp-tools

%description
Giggle is a Gtk frontend to git.

With Giggle you will be able to visualize and browse easily the revision tree,
view changed files and differences between revisions, visualize summarized info
for the project, commit changes and other useful tasks for any git managed
projects contributor.

See http://live.gnome.org/giggle for more information.

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %version-%release
%description devel
%summary

%prep
%setup
%patch

%build
%autoreconf
%configure --disable-static

%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name
%_libdir/lib%name.so.*
%_libdir/lib%name-git.so.*
%_iconsdir/*/*/*/*
%_desktopdir/%name.desktop
%dir %_datadir/%name
%_datadir/%name/*

%files devel
%_libdir/*.so
%_includedir/%name

%changelog
* Fri Mar 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt2
- rebuilt against libgtksourceview-3.0-so.1

* Sat Nov 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt1
- 0.7
- dropped patches
- disabled build with libebook

* Tue Oct 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.6.1-alt3
- fixed build with new libebook

* Thu Mar 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt2
- rebuild against libebook-1.2.so.13

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Fri Oct 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6
- updated buildreqs

* Mon Oct 11 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5-alt2
- rebuild

* Sat Apr 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5-alt1
- New version 0.5

* Sun Mar 14 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.97-alt1
- New version 0.4.97

* Wed Mar 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.96-alt1
- New version 0.4.96
- 001-Replace_deprecated_GtkSourceView_function.patch merged upstream

* Mon Jan 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.91-alt2
- fix build

* Mon Apr 13 2009 Vladimir Lettiev <crux@altlinux.ru> 0.4.91-alt1
- new version
- build devel subpackage

* Wed Jan 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4-alt2
- add missed library to package
- fix #13940

* Tue Dec 25 2007 Eugene Ostapets <eostapets@altlinux.org> 0.4-alt1
- 0.4

* Sun Jun 17 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3-alt1
- new version
- fix 11803

* Mon Apr 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2-alt0.1
- first build
