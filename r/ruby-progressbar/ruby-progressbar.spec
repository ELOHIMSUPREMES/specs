
%define        pkgname progressbar

Name:          ruby-%pkgname
Version:       1.10.0
Release:       alt2
Summary:       Ruby/ProgressBar is a text progress bar library for Ruby.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jfelchner/ruby-progressbar
# VCS:         https://github.com/jfelchner/ruby-progressbar.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
The ultimate text progress bar library for Ruby! It'll SMASH YOU OVER THE HEAD
with a PURE RUSH of progress bar excitement!

Don't miss out on what all the kids are talking about! If you want everyone
to know that your gem or app can survive in the cage then YOU WANT
RUBY-PROGRESSBAR!


%package       -n gem-ruby-%pkgname
Summary:       %summary
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-ruby-%pkgname
%summary


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.


%package       -n gem-ruby-%pkgname-doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-ruby-%pkgname-doc
Documentation files for %{name}.


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

%files         -n gem-ruby-%pkgname
%ruby_gemspecdir/ruby-%pkgname-%version.gemspec
%ruby_gemslibdir/ruby-%pkgname-%version

%files         -n gem-ruby-%pkgname-doc
%ruby_gemsdocdir/ruby-%pkgname-%version


%changelog
* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt2
- Use Ruby Policy 2.0.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus
