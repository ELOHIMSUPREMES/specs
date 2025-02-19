%define        pkgname ruby-dbus

Name:          ruby-dbus
Version:       0.15.0
Release:       alt2
Summary:       Ruby D-BUS library
Group:         Development/Ruby
License:       LGPLv2.1
Url:           https://trac.luon.net/ruby-dbus/
# VCS          https://github.com/mvidner/ruby-dbus.git
BuildArch:     noarch
Source:        %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Ruby D-Bus provides an implementation of the D-Bus protocol such that
the D-Bus system can be used in the Ruby programming language.

%package       doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %name.

%prep
%setup -q -n %pkgname-%version

%build
%gem_build --use=ruby-dbus --alias=dbus

%install
%gem_install

%files
%ruby_gemspec
%ruby_gemlibdir


%files         doc
%ruby_gemdocdir

%changelog
* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt2
- Use setup gem's dependency detection

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt1
- Bump to 0.15.0;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.12-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.2.12-alt1.2
- Rebuild with Ruby 2.4.1

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.2.12-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 0.2.12-alt1
- 0.2.11 -> 0.2.12

* Sat Dec 19 2009 Igor Zubkov <icesik@altlinux.org> 0.2.11-alt1
- 0.2.10 -> 0.2.11

* Sat Oct 31 2009 Igor Zubkov <icesik@altlinux.org> 0.2.10-alt1
- 0.2.1 -> 0.2.10

* Wed Oct 14 2009 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt2
- update setup.rb

* Sat Aug 08 2009 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt1
- build
