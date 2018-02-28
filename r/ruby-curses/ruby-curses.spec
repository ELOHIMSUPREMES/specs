%define  pkgname curses
 
Name: 	 ruby-%pkgname
Version: 1.0.2 
Release: alt1
 
Summary: Ruby binding for curses, ncurses, and PDCurses
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ruby/curses
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libncursesw-devel
 
%description
A Ruby binding for curses, ncurses, and PDCurses. curses is an extension
library for text UI applications.  Formerly part of the Ruby standard
library.

%prep
%setup -n %pkgname-%version
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%changelog
* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build in Sisyphus
