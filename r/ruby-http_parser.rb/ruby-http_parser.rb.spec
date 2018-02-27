%define  pkgname http_parser.rb
 
Name: 	 ruby-%pkgname
Version: 0.6.0 
Release: alt1
 
Summary: A simple callback-based HTTP request/response parser for writing http servers, clients and proxies
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/tmm1/http_parser.rb
 
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source:  %pkgname-%version.tar
Source1: http-parser-2.3.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-benchmark_suite
BuildRequires: ruby-ffi
BuildRequires: libruby-devel

%description
A simple callback-based HTTP request/response parser for writing http
servers, clients and proxies.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
tar xf %SOURCE1

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
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for ALT Linux
