%define        pkgname power-assert
%define        gemname power_assert

Name:          gem-%pkgname
Version:       1.1.4
Release:       alt1
Summary:       Power Assert for Ruby
License:       BSD 2-clause Simplified License/Custom
Group:         Development/Ruby
Url:           https://github.com/k-tsj/power_assert
# VCS:         https://github.com/k-tsj/power_assert.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- Bump to 1.1.4
- Use Ruby Policy 2.0

* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus, packaged as a gem
