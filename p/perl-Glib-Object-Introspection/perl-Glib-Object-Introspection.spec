Name: perl-Glib-Object-Introspection
Version: 0.025
Release: alt1

Summary: Dynamically create Perl language bindings
Group: Development/Perl
License: lgpl

Url: %CPAN Glib-Object-Introspection
Source: %name-%version.tar

BuildRequires: gobject-introspection-devel libcairo-gobject-devel perl-devel perl-ExtUtils-Depends perl-Glib-devel perl-ExtUtils-PkgConfig

%description
%summary

%prep
%setup -q

%build
# some Glib functions fail with LANG=C
export LANG=ru_RU.UTF-8
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Glib/Object/Introspection*
%perl_vendor_archlib/Glib/Object/Introspection*
%doc LICENSE NEWS README

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1.1
- rebuild with new perl 5.20.1

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- automated CPAN update

* Thu May 01 2014 Vladimir Lettiev <crux@altlinux.ru> 0.022-alt1
- 0.022

* Tue Feb 25 2014 Vladimir Lettiev <crux@altlinux.ru> 0.020-alt1
- 0.016 -> 0.020

* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.016-alt1
- initial build for ALTLinux

