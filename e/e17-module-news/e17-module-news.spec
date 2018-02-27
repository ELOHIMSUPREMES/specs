%define _name news

Name: e17-module-%_name
Version: 0.1.0
Release: alt3

Summary: %_name module for the Enlightenment desktop
License: BSD
Group: Graphical desktop/Enlightenment
Url: http://www.enlightenment.org/

#Source: ftp://ftp.enlightenment.org/pub/enlightenment/%_name-%version.tar.gz
Source: %_name-%version.tar

Requires: e17 = %e17_version

BuildRequires: e17-devel
BuildRequires: edje embryo_cc

%description
%_name module for the Enlightenment desktop to display information
feeds like Rss (and soon Atom).

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_libdir/enlightenment/modules/%{_name}*
%doc AUTHORS ChangeLog COPYING* NEWS README

%changelog
* Wed Apr 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt3
- rebuilt for e17-0.17.2.1

* Sat Apr 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt2
- updated from upstream git, built for e17-0.17.1

* Tue Jan 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus

