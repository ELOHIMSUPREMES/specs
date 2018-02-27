Name: perl-AnyEvent-Fork
Version: 1.2
Release: alt1

Summary: everything you wanted to use fork() for, but couldn't
Group: Development/Perl
License: Perl

Url: %CPAN AnyEvent-Fork
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(AnyEvent.pm) perl-devel perl(IO/FDPass.pm) perl(Proc/FastSpawn.pm) perl(common/sense.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/AnyEvent/Fork*
%doc README Changes

%changelog
* Thu Jan 16 2014 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt1
- initial build for ALTLinux

