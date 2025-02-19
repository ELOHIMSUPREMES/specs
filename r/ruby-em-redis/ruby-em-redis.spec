%define  pkgname em-redis

Name: 	 ruby-%pkgname
Version: 0.3.0 
Release: alt1.1

Summary: An eventmachine-based implementation of the Redis protocol
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://github.com/libc/em-redis

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

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
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Oct 18 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
