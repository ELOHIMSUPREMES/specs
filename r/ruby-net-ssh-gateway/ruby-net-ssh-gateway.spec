# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname net-ssh-gateway

Name: ruby-%pkgname
Version: 1.0.1
Release: alt2.2

Summary: A simple library to assist in establishing tunneled Net::SSH connections
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/net-ssh/

BuildArch: noarch

Source0: %pkgname-%version.tar.gz

# Automatically added by buildreq on Sat Dec 05 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
A simple library to assist in establishing tunneled Net::SSH connections.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG.rdoc README.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Net/SSH/Gateway

%changelog
* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2.2
- Rebuild with Ruby 2.4.1

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 11 2009 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt2
- fix License

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt1
- build for Sisyphus

