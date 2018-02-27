%define ver_major 0.1
%def_disable dax

Name: pinpoint
Version: %ver_major.6
Release: alt1

Summary: A tool for making hackers do excellent presentations
Group: Office
License: LGPLv2+
Url: http://wiki.gnome.org/Apps/Pinpoint

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: libgio-devel libcairo-devel libgdk-pixbuf-devel
BuildRequires: libclutter-devel libclutter-gst3.0-devel librsvg-devel
%{?_enable_dax:BuildRequires: libdax-devel libmx-devel}

%description
Pinpoint is a text file driven presentation tool aiming to make
presentations be excellent; striving to reduce death by bullet point.
And to keep peoples interest in what is actually being presented.

%prep
%setup

%build
%autoreconf
%configure \
	%{subst_enable dax}
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_datadir/%name/
%doc AUTHORS NEWS README

%changelog
* Tue Jul 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt2
- updated from upstream git

* Wed Nov 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- first build for Sisyphus

