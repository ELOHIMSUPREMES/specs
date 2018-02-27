%define pkgname kgio

Name: ruby-%pkgname
Version: 2.9.2
Release: alt1

Summary: kinder, gentler I/O for Ruby
Group: Development/Ruby
License: LGPL
Url: http://bogomips.org/kgio/

Source: %pkgname-%version.tar.gz

# Automatically added by buildreq on Wed Aug 10 2011
# optimized out: ruby ruby-stdlibs ruby-tool-rdoc
BuildRequires: libruby-devel ruby-tool-setup strace

%description
kgio provides non-blocking I/O methods for Ruby without raising
exceptions on EAGAIN and EINPROGRESS. It is intended for use with the
Unicorn and Rainbows! Rack servers, but may be used by other
applications (that run on Unix-like platforms).


%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc 
Documentation files for %name.

%prep
%setup -q -n %pkgname-%version
%update_setup_rb

%build 
%ruby_config 
%ruby_build
#for t in test/test_*.rb; do
#ruby_test_unit -Iext/kgio:lib "$t"
#done


%install
%ruby_install
%rdoc lib/

%files
%doc README TODO
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%doc COPYING HACKING ISSUES
%ruby_ri_sitedir/Kgio*

%changelog
* Fri Nov 07 2014 Anton Gorlov <stalker@altlinux.ru> 2.9.2-alt1
- new version

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.7.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 2.7.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Jan 10 2012 Anton Gorlov <stalker@altlinux.ru> 2.7.2-alt1
- new version

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 2.6.0-alt1
- initial build for altlinux
