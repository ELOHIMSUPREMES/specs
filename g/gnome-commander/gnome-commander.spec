%define ver_major 1.4
%def_with exiv2
%def_with chm
%def_with taglib
%def_with poppler
%def_with libgsf

Name: gnome-commander
Version: %ver_major.1
Release: alt1

Summary: A Gnome file manager similar to the Norton Commander (TM)
License: GPL
Group: File tools
Url: http://www.freesoftware.fsf.org/gcmd/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gnome-vfs gnome-vfs-module-sftp gnome-vfs-module-smb

BuildRequires: flex gcc-c++ gnome-doc-utils gnome-doc-utils-xslt intltool
BuildRequires: libgnomeui-devel libgnome-keyring-devel gnome-vfs-devel
BuildRequires: libunique-devel python-devel
%{?_with_exiv2:BuildRequires: libexiv2-devel}
%{?_with_libchm:BuildRequires: libchm-devel}
%{?_with_taglib:BuildRequires: libtag-devel}
%{?_with_poppler:BuildRequires: libpoppler-glib-devel}
%{?_with_libgsf:BuildRequires: libgsf-devel}

%description
Gnome Commander is a file manager that just like the classical Norton Commander (TM)
lets you do everything with the keyboard. It can perform all standard file operations
and some extra features like FTP support.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{subst_with exiv2} \
	%{subst_with libchm} \
	%{subst_with taglib} \
	%{subst_with poppler} \
	%{subst_with libgsf}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libdir/%name/
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_datadir/pixmaps/%name/
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README TODO doc/*.txt

%exclude %_libdir/%name/*.la
%exclude %_libdir/%name/plugins/*.la


%changelog
* Sat Apr 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Mar 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Jan 12 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.8.17-alt1
- 1.2.8.17

* Mon Sep 19 2011 Radik Usupov <radik@altlinux.org> 1.2.8.13-alt1
- New version (1.2.8.13)

* Mon Feb 14 2011 Radik Usupov <radik@altlinux.org> 1.2.8.10-alt1
- New version (1.2.8.10) (Closes: 25083)
  + Bug fixes:
    + Fixed problem #448941 (numeric keypad arrows don't work in the main window)
    + Fixed problem #620275 (add menu item to copy full path and file name to clipboard)
    + Fixed problem #637501 (advrename: metatag popup menu shows wrong items)
    + Fixed problem with toggling path/basename/filename selections in copy/move dialogs
    + Fixed problem with searching path for devices
    + Updated translations: de
  gnome-commander 1.2.8.9
  + New features:
    + Support for shell-style wildcards in quick search
  gnome-commander 1.2.8.8
  + Bug fixes:
    + Fixed problem #610764 (menu item won't stay checked)
    + Fixed problem #626469 (add support for other su-like programs: xdg-su, gnomesu)
    + Fixed problem with broken Spanish translation
- Spec cleaned

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt4.1
- Rebuilt with python 2.6

* Tue Dec 16 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt4
- Some changes in spec file

* Fri Dec 12 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt3
- Add icons

* Thu Nov 20 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt2
- Apply repocop patch

* Fri Sep 26 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt1
- New version 1.2.7

* Fri May 14 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.1.6-alt2
- bug fix compile with gtk 2.4

* Tue Jan 20 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.1.6-alt1
- 1.1.6
- bugs fixes
- updated the cvs-plugin so that it can be used to diff and log files
- made the cwd label selectable (the one left of the cmdline)
- sorting column and direction is now remembered
- added button to the directory indicator to popup the directory history

* Sat Jan 17 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.1.5-alt1
- 1.1.5
- the ext-column is now hidden when the extension is only showed together  with the filename
- fixed unnecessary redraws of the file-list when dragging files over it
- fixed problem with ftp-connections that didn't disappear from the connection toolbars when disconnected
- the program no longer tries to center itself on the desktop
- fixed problems when renaming directories

* Fri Nov 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1.4-alt1
- 1.1.4
- Fixed bug when selecting multiple files with shift+mouse button
- Cleaned up the file-popup menu
- Fixed possible async error when cancelling a xfer operation
- Reworked the layout tab and removed the colors tab in the options dialog
- Improved plugin-system

* Sat Nov 15 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1.3-alt1
- 1.1.3
- Bugs fixed
- Changed base class from GtkDialog to GnomeCmdDialog

* Sun Nov 2 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1.2-alt1
- 1.1.2
- SMB browsing
- Major rewrite of alot of code
- Bugs fixed

* Thu Oct 30 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0.1-alt2
- Update build requires

* Sat Jun 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jun 6 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- Realese 1.0

* Thu Apr 20 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.12-alt2
- Add requires to fam and cleanup spec

* Tue Mar 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.12-alt1
- First version of RPM package.

