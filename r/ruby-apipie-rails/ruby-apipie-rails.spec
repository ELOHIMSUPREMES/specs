%define        pkgname apipie-rails

Name:          ruby-%pkgname
Version:       0.5.15
Release:       alt1
Summary:       Ruby on Rails API documentation tool
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/Apipie/apipie-rails
# VCS:         https://github.com/Apipie/apipie-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Apipie-rails is a DSL and Rails engine for documenting your RESTful API. Instead
of traditional use of #comments, Apipie lets you describe the code, through
the code. This brings advantages like:

* No need to learn yet another syntax, you already know Ruby, right?
* Possibility of reusing the docs for other purposes (such as validation)
* Easier to extend and maintain (no string parsing involved)
* Possibility of reusing other sources for documentation purposes (such as
  routes etc.)

The documentation is available from within your app (by default under
the /apipie path.) In development mode, you can see the changes as you go. It's
markup language agnostic, and even provides an API for reusing the documentation
data in JSON.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.15-alt1
- Bump to 0.5.15
- Use Ruby Policy 2.0

* Wed Oct 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.5.13-alt1
- Bump to 0.5.13

* Wed Oct 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.12-alt1
- New version.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.11-alt1
- New version.

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 0.5.10-alt2
- Gemify the package.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.10-alt1
- New version.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.9-alt1
- New version.
- Package as gem.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.8-alt1
- Initial build for Sisyphus
