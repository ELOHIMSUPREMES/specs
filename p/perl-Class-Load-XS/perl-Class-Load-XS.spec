Name: perl-Class-Load-XS
Version: 0.06
Release: alt1

Summary: XS implementation of parts of Class::Load
Group: Development/Perl
License: artistic_2

Url: %CPAN Class-Load-XS
Source: %name-%version.tar

BuildRequires: perl(Test/Requires.pm) perl(Class/Load.pm) perl(Test/Fatal.pm) perl-devel perl(Module/Implementation.pm) perl(Module/Build.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Class/Load/XS*
%perl_vendor_archlib/Class/Load/XS*
%doc Changes LICENSE README

%changelog
* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- initial build for ALTLinux

