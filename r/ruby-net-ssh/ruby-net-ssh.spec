%define        pkgname net-ssh

Name:          ruby-%pkgname
Version:       4.2.0
Release:       alt3
Epoch:         1
Summary:       Pure-Ruby implementation of the SSH2 client protocol
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/net-ssh/net-ssh
# VCS:         https://github.com/net-ssh/net-ssh.git
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-mocha

%description
Net::SSH is a pure-Ruby implementation of the SSH2 client protocol. It
allows you to write programs that invoke and interact with processes on
remote servers, via SSH2.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation

%description   doc
Documentation files for %name


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
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 1:4.2.0-alt3
- Use Ruby Policy 2.0.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:4.2.0-alt2
- Reset to old version for chef and ruby-specinfra.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Thu Dec 06 2012 Led <led@altlinux.ru> 2.0.15-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Thu Nov 19 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.15-alt1
- [2.0.15]

* Fri Aug 07 2009 Konstantin Pavlov <thresh@altlinux.org> 2.0.11-alt1
- 2.0.11 release.

* Wed Nov 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.0.4-alt1
- Initial build for ALT Linux.

