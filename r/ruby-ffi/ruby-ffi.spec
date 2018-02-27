# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname ffi

Name: ruby-%pkgname
Version: 1.9.6
Release: alt1

Summary: Ruby foreign function interface
Group: Development/Ruby
License: BSD
Url: https://github.com/ffi/ffi

Source: %pkgname-%version.tar

# Automatically added by buildreq on Sun Jun 28 2009 (-bi)
BuildRequires: libffi-devel libruby-devel ruby-tool-setup

%description
A Ruby foreign function interface.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

sed -i -r '/^[[:blank:]]*Data_Get_Struct\(/s/^(([[:blank:]]*).*)((field) = layout->fields\[i\])(\).*)$/\2\3;\n\1\4\5/' \
	ext/ffi_c/StructLayout.c

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
%doc README.md LICENSE
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.6-alt1
- New version
- Fix project URL

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.6.3-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.6.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed build

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.3-alt1
- 0.6.3
- Rebuild with new libffi

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.5-alt1
- Built for Sisyphus

