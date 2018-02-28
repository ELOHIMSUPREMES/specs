
Name:           pcsc-tools
Version:        1.4.24
Release:        alt1
Summary:        Tools to be used with smart cards and PC/SC

Group:          System/Configuration/Hardware
License:        GPLv2+
URL:            http://ludovic.rousseau.free.fr/softwares/pcsc-tools/
Source0:        http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libpcsclite-devel >= 1.2.9
BuildRequires:  perl-pcsc
BuildRequires:  perl-Gtk2
Requires:       pcsc-lite

%description
The pcsc-tools package contains some useful tools for a PC/SC user:
pcsc_scan regularly scans connected PC/SC smart card readers and
prints detected events, ATR_analysis analyzes smart card ATRs (Anwser
To Reset), scriptor sends commands to a smart card.

%package gui
Summary:	GUI tool to be used with smart cards and PC/SC
Group:          System/Configuration/Hardware
Requires:	pcsc-tools = %version-%release

%description gui
The pcsc-tools-gui package contains gscriptor sends commands to a smart
card from a GTK user interface.

%prep
%setup -q
subst 's/-O2 -g/$(RPM_OPT_FLAGS)/' Makefile

%build
%make_build

%install
%make_install install DESTDIR=%buildroot%_prefix
desktop-file-install --mode=644 \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications gscriptor.desktop
# TODO: icon

%files
%doc Changelog LICENCE README TODO
%_bindir/*
%_datadir/pcsc/
%doc %_man1dir/*
%exclude %_bindir/gscriptor
%exclude %_man1dir/gscriptor.*

%files gui
%_bindir/gscriptor
%_desktopdir/gscriptor.desktop
%doc %_man1dir/gscriptor.*

%changelog
* Wed Sep 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.24-alt1
- New version

* Mon Feb 02 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.23-alt1
- New version

* Wed Feb 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.4.22-alt1
- Initial build for ALT Linux (thanks Fedora for spec)

