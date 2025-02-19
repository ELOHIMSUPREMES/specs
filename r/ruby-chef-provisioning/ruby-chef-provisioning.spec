%define        pkgname chef-provisioning

Name:          ruby-%pkgname
Version:       2.7.6
Release:       alt1
Summary:       A library for creating machines and infrastructures idempotently in Chef.
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-provisioning
# VCS:         https://github.com/chef/chef-provisioning.git
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
%ruby_gemspec
%ruby_gemlibdir/*

%files         doc
%ruby_gemdocdir/*

%changelog
* Tue Feb 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1
- Bump to 2.7.6
- Use Ruby Policy 2.0

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- Initial build for Sisyphus
