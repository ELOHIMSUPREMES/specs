%define        pkgname kgio

Name:          ruby-%pkgname
Version:       2.11.2
Release:       alt4
Summary:       kinder, gentler I/O for Ruby
Group:         Development/Ruby
License:       LGPLv2
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://bogomips.org/kgio
# VCS:         https://bogomips.org/kgio.git
Source:        %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(olddoc)

%description
kgio provides non-blocking I/O methods for Ruby without raising
exceptions on EAGAIN and EINPROGRESS. It is intended for use with the
Unicorn and Rainbows! Rack servers, but may be used by other
applications (that run on Unix-like platforms).


%package       devel
Summary:       Development files for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %name.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %name.


%prep
%setup -n %pkgname-%version

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         devel
%ruby_includedir/*

%files         doc
%ruby_gemdocdir

%changelog
* Fri Feb 01 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt4
- Use Ruby Policy 2.0.

* Wed Jan 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt3
- Place library into proper ruby gem folder.

* Thu Nov 15 2018 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt2
- Fix binding with compiled binary so-libs.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.1
- Rebuild with Ruby 2.5.0

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- new version 2.11.0

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- new version 2.10.0

* Fri Nov 07 2014 Anton Gorlov <stalker@altlinux.ru> 2.9.2-alt1
- new version

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.7.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 2.7.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Jan 10 2012 Anton Gorlov <stalker@altlinux.ru> 2.7.2-alt1
- new version

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 2.6.0-alt1
- initial build for altlinux
