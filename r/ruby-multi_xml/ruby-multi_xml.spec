%define  pkgname multi_xml

Name:    ruby-%pkgname
Version: 0.6.0
Release: alt1

Summary: A generic swappable back-end for XML parsing
License: MIT
Group:   Development/Ruby
Url:     https://github.com/sferik/multi_xml

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

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
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
