%define  pkgname multi_json
 
Name: 	 ruby-%pkgname
Version: 1.9.2 
Release: alt1
 
Summary: A common interface to multiple JSON libraries
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://github.com/intridea/multi_json
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: yajl-ruby
BuildRequires: ruby-json-pure
BuildRequires: ruby-oj

%description
A common interface to multiple JSON libraries, including Oj, Yajl, the
JSON gem (with C-extensions), the pure-Ruby JSON gem,
NSJSONSerialization, gson.rb, JrJackson, and OkJson.

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
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt1
- Initial build for ALT Linux
