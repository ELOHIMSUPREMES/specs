%define        pkgname chef-zero

Name: 	       %pkgname
Version:       14.0.12
Release:       alt1
Summary:       Self-contained, easy-setup, fast-start in-memory Chef server for testing and solo setup purposes
License:       Apache 2.0
Group:         Development/Ruby
Url:           http://www.opscode.com/
# VCS:         https://github.com/chef/chef-zero
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi-yajl)
BuildRequires: ruby-mixlib-log
BuildRequires: ruby-hashie
BuildRequires: ruby-uuidtools

%description
Chef Zero is a simple, easy-install, in-memory Chef server that can be useful
for Chef Client testing and chef-solo-like tasks that require a full Chef
Server. It IS intended to be simple, Chef 11+ compliant, easy to run and fast to
start. It is NOT intended to be secure, scalable, performant or persistent. It
does NO input validation, authentication or authorization (it will not throw a
400, 401 or 403). It does not save data, and will start up empty each time you
start it.

Because Chef Zero runs in memory, it's super fast and lightweight. This makes it
perfect for testing against a "real" Chef Server without mocking the entire
Internet.


%package       -n gem-%pkgname
Summary:       Library files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname
Library files for %gemname gem.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Obsoletes:     %pkgname-doc
Provides:      %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files         -n gem-%pkgname
%ruby_gemlibdir
%ruby_gemspec

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files
%_bindir/chef-zero

%changelog
* Mon Apr 08 2019 Pavel Skrylev <majioa@altlinux.org> 14.0.12-alt1
- Bump to 14.0.12
- Fix spec

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 14.0.11-alt2
- Use Ruby Policy 2.0.

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.11-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.8-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.6-alt1
- New version.

* Sun Apr 22 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.5-alt1
- New version.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.2-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- New version.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Jul 18 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version

* Wed Mar 29 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.2-alt1
- New version

* Tue Mar 21 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- new version 5.2.0

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Fri Aug 21 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 4.0-alt1
- Initial build for ALT Linux
