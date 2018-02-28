Name: wmforecast
Version: 0.10
Release: alt1

Summary: weather dockapp for Window Maker using the Yahoo Weather API
License: GPLv3+, CC-BY-SA-3.0 (icons)
Group: Graphical desktop/Window Maker

# https://github.com/d-torrance/wmforecast
Url: http://www.friedcheese.org/wmforecast/
Source0: %name-%version.tar
Source100: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu Feb 11 2016 (-bi)
# optimized out: elfutils fontconfig libX11-devel libwraster-devel pkg-config python-base xorg-xproto-devel xz
BuildRequires: libWINGs-devel libcurl-devel libxml2-devel

BuildRequires: help2man

%description
wmforecast is a weather dockapp for Window Maker.
It displays the current temperature and an icon representing
the current conditions.  A balloon tooltip displays forecast
information.  The weather information comes from the
Yahoo Weather API.

%prep
%setup
sed -ri 's/^(Exec=.*$)/& --units c/' %name.desktop
sed -ri 's/units = ("*)f("*)/units = \1c\2/' %name.[1c]*
sed -i  's/2502265/2122265/g' %name.[1c]*
sed -i  's/Sunnyvale, CA/Moscow, Russia/' %name.1*

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS
%_man1dir/*
%_bindir/*
%_datadir/%name/
%_desktopdir/*
%_liconsdir/*.png
%_iconsdir/*/*/*/*.svg

%changelog
* Thu Mar 31 2016 Michael Shigorin <mike@altlinux.org> 0.10-alt1
- 0.10

* Thu Feb 11 2016 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- initial release (thanks Debian for packaging bits)
  + adapted for ALT Linux
