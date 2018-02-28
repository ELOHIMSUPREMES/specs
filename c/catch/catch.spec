Name: catch
Version: 1.4.0
Release: alt1

Summary: C++ Unit Test framework ("all in one header")

License: GPL
Group: Development/C++
Url: https://github.com/philsquared/Catch

Packager: Pavel Vainerman <pv@altlinux.ru>
BuildArch: noarch

# Git: https://github.com/philsquared/Catch
Source: %name-%version.tar

#BuildRequires:

%description
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%prep
%setup 

%build

%install
mkdir -p %buildroot%_includedir
mv -f single_include/catch.hpp %buildroot%_includedir

%files
%_includedir/*.hpp

%changelog
* Fri Mar 18 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.0-alt1
- build new version

* Tue Mar 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.3.5-alt1
- build new version

* Fri Feb 19 2016 Pavel Vainerman <pv@altlinux.ru> 1.3.4-alt1
- build new version

* Wed Dec 16 2015 Pavel Vainerman <pv@altlinux.ru> 1.3.1-alt1
- build new version

* Mon Oct 26 2015 Pavel Vainerman <pv@altlinux.ru> 1.2.1-alt3
- spec: fix URL for project

* Mon Oct 26 2015 Pavel Vainerman <pv@altlinux.ru> 1.2.1-alt2
- new build (merge changes from master repository)

* Tue Jun 30 2015 Pavel Vainerman <pv@altlinux.ru> 1.2.1-alt1
- new version

* Wed May 13 2015 Pavel Vainerman <pv@altlinux.ru> 1.1-alt2
- rebuild (new .gear/rules)

* Mon Mar 30 2015 Pavel Vainerman <pv@altlinux.ru> 1.1-alt1
- new upstream version

* Mon Oct 06 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1.2
- test rebuild

* Fri Oct 03 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1.1
- rename package Catch --> catch

* Thu Oct 02 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1
- moved catch.hpp directly into %_includedir

* Tue Sep 30 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt0.2
- test build

* Tue Sep 30 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt0.1
- initial commit
