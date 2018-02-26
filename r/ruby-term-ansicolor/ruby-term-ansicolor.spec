Name: ruby-term-ansicolor
Version: 1.0.4
Release: alt1.1

Summary: Ruby library that colors strings using ANSI escape sequences
Group: Development/Ruby
License: GPLv2
Url: http://term-ansicolor.rubyforge.org

Source0: term-ansicolor-%version.tgz

BuildArch: noarch

# Automatically added by buildreq on Fri Dec 25 2009 (-bi)
BuildRequires: rpm-build-ruby

%description
Ruby library that colors strings using ANSI escape sequences.

%prep
%setup -q -n term-ansicolor-%version

%build

%install
mkdir -p %buildroot%ruby_sitelibdir/term/ansicolor/
install -p -m644 lib/term/ansicolor.rb %buildroot%ruby_sitelibdir/term/
install -p -m644 lib/term/ansicolor/version.rb %buildroot%ruby_sitelibdir/term/ansicolor/

%files
%doc CHANGES README doc-main.txt examples
%ruby_sitelibdir/term/

%changelog
* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.4-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 25 2009 Igor Zubkov <icesik@altlinux.org> 1.0.4-alt1
- build for Sisyphus

