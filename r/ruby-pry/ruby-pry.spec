%define  pkgname pry

Name: 	 ruby-%pkgname
Version: 0.10.4 
Release: alt3

Summary: An IRB alternative and runtime developer console
License: MIT
Group:   Development/Ruby
Url:     https://github.com/pry/pry

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

%filter_from_requires /^ruby(win32console)$/d

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Requires: ruby-slop3

%description
Pry is a powerful alternative to the standard IRB shell for Ruby. It is written
from scratch to provide a number of advanced features.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
install -Dm755 bin/%pkgname %buildroot%_bindir/%pkgname
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%_bindir/%pkgname

%changelog
* Mon May 29 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.10.4-alt3
- Remove doc package because exists pry-doc -- documentation plugin for pry

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.10.4-alt2
- Add requires to ruby-slop3

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.10.4-alt1
- Initial build in Sisyphus
