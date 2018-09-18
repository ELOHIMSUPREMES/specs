%define  pkgname specinfra

Name:    ruby-%pkgname
Version: 2.76.1
Release: alt1

Summary: Command Execution Framework for serverspec, itamae and so on
License: MIT
Group:   Development/Ruby
Url:     https://github.com/mizzy/specinfra

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
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.76.1-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.73.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.73.4-alt1
- New version.
- Package as gem.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.73.3-alt1
- Initial build for Sisyphus
