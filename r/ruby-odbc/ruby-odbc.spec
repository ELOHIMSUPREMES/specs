%define        pkgname ruby-odbc
%define        gemname ruby-odbc

Name:          %pkgname
Version:       0.99999
Release:       alt1
Summary:       ODBC extension for Ruby
License:       GPL
Group:         Development/Ruby
Url:           http://www.ch-werner.de/rubyodbc
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libunixODBC-devel

%description
This is an ODBC binding for Ruby. So far it has been tested with
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (local), unixODBC 2.1.0 on Linux 2.2-x86
 - Ruby 1.6.4, MySQL 3.22/MyODBC (local), libiodbc 2.50 on Linux 2.2-x86
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (remote), MS Jet Engine, MSVC++ 6.0
   on Windows NT4SP6
 - Ruby 1.6.[3-5], MySQL 3.22/MyODBC (remote), MS Jet Engine, cygwin,
   on Windows NT4SP6 and 2000
 - Ruby 1.8.4, SQLite/ODBC 0.67, libiodbc 3.52.4 on Fedora Core 3 x86


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build --use=ruby-odbc --alias=odbc --join=lib:bin

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.99999-alt1
- Bump to 0.99999
- Use Ruby Policy 2.0

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1
- New version
- Rebuild with new %%ruby_sitearchdir location

* Thu Sep 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.99997-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.99992-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.99992-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.99992-alt1
- 0.99992 release.

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9997-alt1
- 0.9997 release.
- Also build UTF-8 version.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9995-alt1
- 0.9995 release.

* Wed Jan 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9994-alt1
- 0.9994 release.

* Fri Dec 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.9993-alt1
- Initial ALTLinux package.
